"""Generate the branded charts and social-preview image used in the README."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw" / "abc_employee_attrition.csv"
IMAGE_DIR = ROOT / "images"

DARK = "#0d0d0d"
OFF_WHITE = "#f4f0e8"
GREY = "#a9a7a2"
GOLD = "#c69a4b"
GRID = "#333333"


def finish_chart(fig: plt.Figure, path: Path) -> None:
    """Save a chart with consistent spacing and resolution."""
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def style_axis(ax: plt.Axes) -> None:
    """Apply the Wilson Moses dark visual system to one axis."""
    ax.set_facecolor(DARK)
    ax.tick_params(colors=OFF_WHITE, labelsize=10)
    ax.xaxis.label.set_color(GREY)
    ax.yaxis.label.set_color(GREY)
    ax.title.set_color(OFF_WHITE)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(axis="y", color=GRID, linewidth=0.7, alpha=0.65)
    ax.set_axisbelow(True)


def create_social_preview() -> None:
    """Create a 1280 × 640 GitHub social-preview card."""
    fig = plt.figure(figsize=(8, 4), dpi=160, facecolor=DARK)
    canvas = fig.add_axes((0, 0, 1, 1))
    canvas.set_axis_off()
    canvas.add_patch(
        plt.Rectangle((0.065, 0.12), 0.008, 0.76, transform=canvas.transAxes, color=GOLD)
    )

    fig.text(0.10, 0.77, "PEOPLE ANALYTICS  |  WEEK 1", color=GOLD, fontsize=12, weight="bold")
    fig.text(0.10, 0.58, "EMPLOYEE ATTRITION", color=OFF_WHITE, fontsize=28, weight="bold")
    fig.text(0.10, 0.45, "EXPLORATORY ANALYSIS", color=OFF_WHITE, fontsize=24, weight="bold")
    fig.text(
        0.10,
        0.30,
        "1,470 employee records  •  35 variables  •  business-focused insights",
        color=GREY,
        fontsize=10,
    )
    fig.text(0.10, 0.17, "WILSON MOSES  |  DATA SCIENCE × AI ENGINEERING", color=GOLD, fontsize=10)
    fig.text(0.88, 0.48, "WM", color=GOLD, fontsize=38, weight="bold", ha="center")

    fig.savefig(IMAGE_DIR / "social-preview.png", facecolor=DARK)
    plt.close(fig)


def create_overall_attrition(data: pd.DataFrame) -> None:
    """Chart retained and departed employee counts."""
    counts = data["Attrition"].value_counts().reindex(["No", "Yes"])
    labels = ["Stayed", "Left"]
    percentages = counts.div(len(data)).mul(100)

    fig, ax = plt.subplots(figsize=(8, 4.8), facecolor=DARK)
    bars = ax.bar(labels, counts.values, color=[GREY, GOLD], width=0.56)
    style_axis(ax)
    ax.set_title("Overall employee attrition", fontsize=17, weight="bold", pad=18)
    ax.set_ylabel("Employees")
    ax.set_ylim(0, counts.max() * 1.18)

    for bar, count, rate in zip(bars, counts.values, percentages.values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + counts.max() * 0.025,
            f"{count:,}  ({rate:.1f}%)",
            ha="center",
            color=OFF_WHITE,
            fontsize=11,
            weight="bold",
        )

    finish_chart(fig, IMAGE_DIR / "overall-attrition.png")


def create_overtime_chart(data: pd.DataFrame) -> None:
    """Compare attrition rates for employees with and without overtime."""
    rates = (
        pd.crosstab(data["OverTime"], data["Attrition"], normalize="index")["Yes"]
        .mul(100)
        .reindex(["No", "Yes"])
    )
    overall_rate = data["Attrition"].eq("Yes").mean() * 100

    fig, ax = plt.subplots(figsize=(8, 4.8), facecolor=DARK)
    bars = ax.bar(["No overtime", "Overtime"], rates.values, color=[GREY, GOLD], width=0.56)
    style_axis(ax)
    ax.set_title("Attrition rate by overtime status", fontsize=17, weight="bold", pad=18)
    ax.set_ylabel("Attrition rate (%)")
    ax.set_ylim(0, 36)
    ax.axhline(overall_rate, color=OFF_WHITE, linestyle="--", linewidth=1.1, alpha=0.75)
    ax.text(1.48, overall_rate + 0.8, f"Overall: {overall_rate:.2f}%", color=OFF_WHITE, ha="right")

    for bar, rate in zip(bars, rates.values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            rate + 1,
            f"{rate:.2f}%",
            ha="center",
            color=OFF_WHITE,
            fontsize=11,
            weight="bold",
        )

    finish_chart(fig, IMAGE_DIR / "overtime-attrition-rate.png")


def create_job_role_chart(data: pd.DataFrame) -> None:
    """Rank job roles by observed attrition rate."""
    rates = (
        pd.crosstab(data["JobRole"], data["Attrition"], normalize="index")["Yes"]
        .mul(100)
        .sort_values()
    )
    colors = [GREY] * len(rates)
    colors[-1] = GOLD

    fig, ax = plt.subplots(figsize=(9, 6.2), facecolor=DARK)
    bars = ax.barh(rates.index, rates.values, color=colors, height=0.62)
    style_axis(ax)
    ax.grid(axis="x", color=GRID, linewidth=0.7, alpha=0.65)
    ax.grid(axis="y", visible=False)
    ax.set_title("Observed attrition rate by job role", fontsize=17, weight="bold", pad=18)
    ax.set_xlabel("Attrition rate (%)")
    ax.set_xlim(0, 45)

    for bar, rate in zip(bars, rates.values):
        ax.text(
            rate + 0.7,
            bar.get_y() + bar.get_height() / 2,
            f"{rate:.2f}%",
            va="center",
            color=OFF_WHITE,
            fontsize=9,
        )

    finish_chart(fig, IMAGE_DIR / "job-role-attrition-rate.png")


def main() -> None:
    """Generate all README assets."""
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    data = pd.read_csv(DATA_PATH)
    create_social_preview()
    create_overall_attrition(data)
    create_overtime_chart(data)
    create_job_role_chart(data)


if __name__ == "__main__":
    main()
