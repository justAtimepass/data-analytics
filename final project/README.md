# HR Analytics: Workforce & Attrition Analysis

## Project overview
This end-to-end Data Analytics capstone demonstrates data inspection, cleaning, exploratory data analysis (EDA), visualizations, business insights, and a Power BI dashboard workflow.

> **Dataset disclosure:** The included dataset is synthetic, generated for educational purposes. It does not represent a real employer or real employees. Findings are illustrative, not factual business claims.

## Problem statement
How can HR teams monitor workforce composition and explore possible relationships between attrition, overtime, job satisfaction, tenure, department, and monthly income?

## Dataset description
- Raw file: `hr_analytics_dataset.csv`
- Clean file: `hr_analytics_cleaned.csv`
- Raw rows: 502 (includes intentionally introduced duplicate rows)
- Clean employee records: 500
- Columns: EmployeeID, Age, Gender, Department, JobRole, MonthlyIncome, YearsAtCompany, JobSatisfaction, WorkLifeBalance, OverTime, BusinessTravel, PerformanceRating, Attrition
- A small number of missing values and duplicate rows are deliberately included to demonstrate cleaning.

## Tools used
Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook, Power BI Desktop, Git, GitHub.

## Repository structure
```text
HR_Analytics_Final_Project/
├── hr_analytics_dataset.csv
├── hr_analytics_cleaned.csv
├── HR_Analytics_Project.ipynb
├── hr_analytics_analysis.py
├── README.md
├── HR_Analytics_Project_Report.docx
├── HR_Analytics_Project_Presentation.pptx
├── visualizations/
├── powerbi/
│   └── POWER_BI_DASHBOARD_GUIDE.md
└── GIT_WORKFLOW.md
```

## Data cleaning process
1. Inspected shape, columns, data types, missing values, and descriptive statistics.
2. Removed exact duplicate rows.
3. Imputed missing `MonthlyIncome` and `JobSatisfaction` values using each column's median.
4. Converted cleaned values to integer types.
5. Added `AttritionFlag` and `OverTimeFlag` for analysis.
6. Exported the cleaned data for Power BI.

## EDA
The notebook includes descriptive statistics, department-level summaries, correlation heatmap, IQR-based income outlier screening, and subgroup attrition comparisons.

## Visualizations
Six PNG charts are provided in `visualizations/`:
- Attrition rate by department
- Attrition rate by overtime
- Average monthly income by department
- Job satisfaction distribution
- Average tenure by attrition status
- Age versus monthly income

## Power BI dashboard
Follow `powerbi/POWER_BI_DASHBOARD_GUIDE.md` to import the cleaned CSV, create DAX measures, add KPI cards and visuals, add slicers, and save the `.pbix` file.

## Key insights
The exact metrics are calculated from the supplied synthetic dataset and can be reproduced by running the notebook. Compare attrition by department, overtime, satisfaction, and tenure before making recommendations.

## Business recommendations
1. Investigate departments with above-average attrition; conduct structured stay interviews and review role-specific workload and career paths.
2. Review overtime patterns and workload allocation; pilot workload balancing and monitor attrition before/after.
3. Monitor low job satisfaction and early-tenure employee groups with periodic pulse surveys and onboarding check-ins.

These are hypotheses for investigation, not causal conclusions. The data is synthetic and observational.

## GitHub workflow
See `GIT_WORKFLOW.md` for clone, add, commit, pull, and push commands plus three meaningful commit examples.

## Conclusion
This project demonstrates a complete beginner-friendly analytics workflow from raw data through cleaning, EDA, visualization, dashboard design, and evidence-informed recommendations. Replace the synthetic data with an authorized real dataset if your instructor requires real-world data.
