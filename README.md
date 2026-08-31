# Employee Attrition Analysis

> Exploratory analysis of 1,470 employee records to identify workforce attrition patterns and establish evidence for future statistical or predictive work.

**Programme:** AnalystLab Africa Data Science Internship — Week 1  
**Project phase:** Completed exploratory analysis  
**Author:** [Wilson Moses](https://github.com/WilsonMoses-Data)

## Project overview

ABC Manufacturing Ltd wants to understand employee attrition before investing in predictive modelling. This project examines workforce composition and compares attrition across overtime status, departments, job roles, age, income, and experience.

The analysis is descriptive and exploratory. It identifies associations and priority questions; it does not claim that the observed factors cause employees to leave.

## Business questions

1. What does the workforce look like?
2. Which departments and roles have the highest attrition rates?
3. How does overtime relate to attrition?
4. How do age, monthly income, and working experience differ between employees who stayed and left?
5. Which variables warrant future statistical testing and predictive modelling?

## Dataset

- **Source:** [IBM HR Analytics Employee Attrition & Performance — Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- **Rows:** 1,470 employee records
- **Variables:** 35
- **Target:** `Attrition` (`Yes`/`No`)
- **Missing values found:** 0
- **Exact duplicates found:** 0

The fields cover demographics, compensation, work characteristics, satisfaction measures, job roles, and tenure.

## Workflow

1. Load and inspect the dataset.
2. Validate dimensions, data types, missingness, duplicates, and category values.
3. Summarise workforce composition.
4. Visualise distributions for age, income, and experience.
5. Calculate overall and subgroup attrition rates.
6. Compare employees who stayed and left.
7. Translate the patterns into business insights and future analytical questions.

## Key findings

| Finding | Evidence |
|---|---|
| Overall attrition | 237 of 1,470 employees; **16.12%** |
| Overtime | **30.53%** attrition with overtime vs. **10.44%** without overtime |
| Department | Sales **20.63%**, Human Resources **19.05%**, R&D **13.84%** |
| Highest-risk role | Sales Representative **39.76%** |
| Age | Employees who left averaged approximately **33.6 years** vs. **37.6 years** for those who stayed |
| Monthly income | Employees who left averaged approximately **4,787** vs. **6,833** for those who stayed |
| Total working years | Employees who left averaged approximately **8.2 years** vs. **11.9 years** for those who stayed |

Overtime is the clearest descriptive signal in this analysis, but it should be examined alongside job role, department, travel, satisfaction, and tenure before any intervention is designed.

## Business interpretation

- Review overtime practices and workload concentration, especially in roles with high attrition.
- Investigate Sales Representative working conditions, onboarding, management support, and career progression.
- Segment future analysis by role and department to avoid broad company-wide conclusions.
- Use interviews, exit feedback, and operational context to complement the dataset.
- Validate observed patterns statistically before using them for policy or prediction.

## Repository contents

```text
ABC_Manufacturing_Attrition_Analysis/
├── README.md
├── LICENSE
├── ABC Manufacturing - Attrition Findings & Insights.pptx
└── ABC Data Inspection and Exploration/
    ├── ABC_Employee_Attrition_DataSet.csv
    ├── Data_loading_and_Inspection.ipynb
    └── Data_Exploration.ipynb
```

### Key files

- [`Data_loading_and_Inspection.ipynb`](ABC%20Data%20Inspection%20and%20Exploration/Data_loading_and_Inspection.ipynb) — structural and quality assessment.
- [`Data_Exploration.ipynb`](ABC%20Data%20Inspection%20and%20Exploration/Data_Exploration.ipynb) — visual and attrition-focused analysis.
- [`ABC Manufacturing - Attrition Findings & Insights.pptx`](ABC%20Manufacturing%20-%20Attrition%20Findings%20%26%20Insights.pptx) — presentation of findings and recommendations.

## Tools used

- Python and Jupyter Notebook
- pandas and NumPy
- Matplotlib and Seaborn

## Reproducing the analysis

1. Clone the repository.
2. Create a Python environment.
3. Install Jupyter, pandas, NumPy, Matplotlib, and Seaborn.
4. Open the notebooks in `ABC Data Inspection and Exploration/`.
5. Run `Data_loading_and_Inspection.ipynb` first.
6. Run `Data_Exploration.ipynb` second.

The repository should add a pinned dependency file to improve reproducibility.

## Limitations

- The data is cross-sectional and does not establish causation.
- The analysis does not yet control for interactions between overtime, role, income, tenure, and other factors.
- Several employee-experience variables are self-reported or ordinal.
- Findings from the public IBM dataset may not generalise to another company without local validation.
- Any future model should be assessed for fairness and should support—not replace—human HR judgement.

## Next steps

- Add statistical tests and effect-size estimates for priority relationships.
- Develop multivariate analysis to separate overlapping factors.
- Add a small selection of exported charts to the README.
- Create a reproducible dependency file.
- Rename and reorganise files into consistent `data/`, `notebooks/`, `reports/`, and `images/` folders.

## Licence and data source

Original code and documentation are released under the repository’s [MIT Licence](LICENSE). The dataset remains subject to the terms of its [original Kaggle source](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset).

## Contact

**Wilson Moses** — Data Scientist × AI Engineer in development  
[LinkedIn](https://www.linkedin.com/in/wilson-moses-9207b22bb) · [GitHub](https://github.com/WilsonMoses-Data) · [Moses Learns Data](https://www.tiktok.com/@moses.learnsdata)
