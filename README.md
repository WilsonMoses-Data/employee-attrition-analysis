# ABC Manufacturing Ltd — Employee Attrition Analysis

Week 1 project for the **AnalystLab Africa Data Science Internship Programme**: Business Understanding & Data Exploration.

## Business Scenario

ABC Manufacturing Ltd has engaged AnalystLab Africa Consulting to investigate employee attrition. The HR department wants to understand *why* employees are leaving before investing in predictive machine learning models. This repository contains the exploratory data analysis (EDA) that lays the groundwork for that future model.

## Business Questions

1. What does the company's workforce look like?
2. Which departments have the highest employee attrition?
3. Does age influence attrition?
4. Does monthly income affect retention?
5. Does overtime influence attrition?
6. Which job roles experience the highest turnover?
7. Which variables appear important for future predictive modelling?

## Dataset

[IBM HR Analytics – Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) — 1,470 employee records across 35 attributes (demographics, compensation, role, and satisfaction data).

## Repository Contents

| File | Description |
|---|---|
| `ABC_Manufacturing_Attrition_EDA_PeoMoses.ipynb` | Full exploratory data analysis notebook — inspection, visualisations, and attrition-focused breakdowns |
| `ABC_Manufacturing_Attrition_VisualisationProcess_PeoMoses.docx` | Step-by-step documentation of the visualisation methodology |
| `ABC_Manufacturing_Attrition_FindingsInsights_PeoMoses.pptx` | Slide deck presenting the key findings and business insights |
| `ABC_Employee_Attrition_DataSet.csv` | Source dataset used by the notebook |

## Key Findings

- **Overall attrition rate: 16.1%** (237 of 1,470 employees)
- **Overtime is the strongest single driver** — 30.5% attrition among employees who work overtime vs. 10.4% among those who don't (a 20-point gap)
- **Sales (20.6%) and Human Resources (19.1%)** have the highest departmental attrition; **Research & Development (13.8%)** the lowest
- **Sales Representatives (39.8%)** have by far the highest attrition by job role; **Research Directors (2.5%)** the lowest
- Employees who left skew **younger** (33.6 vs. 37.6 years), **lower-paid** (avg. 4,787 vs. 6,833 monthly income), and **less tenured** (8.2 vs. 11.9 total working years) than employees who stayed

## Tools & Libraries

- Python 3.13
- pandas, matplotlib, seaborn
- PyCharm (Jupyter integration)

## Author

**Peo Moses** — Junior Data Scientist, AnalystLab Africa Consulting
Data Science Internship Programme · Week 1

---
*This analysis is descriptive/exploratory. Associations identified here are candidates for statistical validation and feature selection in a future predictive modelling phase.*
