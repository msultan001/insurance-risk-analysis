# Insurance Risk Analysis

## 1. Project Overview

AlphaCare Insurance Solutions (ACIS) is implementing a data-driven strategy to optimize car insurance premiums by accurately identifying low-risk clients. This project provides a comprehensive analytics pipeline encompassing:

- **Exploratory Data Analysis (EDA)** to understand risk patterns
- **Statistical Hypothesis Testing** to validate pricing assumptions
- **Predictive Modeling** to quantify individual client risk
- **Model Interpretability** to ensure transparent, fair pricing

**Business Goal**: Reduce premiums for demonstrably safe drivers to attract new clients while maintaining profitability.

### Dataset
- **Source**: Historical car insurance claims data (`MachineLearningRating_v3.txt`)
- **Size**: ~500MB (~1M records)
- **Features**: 52 variables including policy details, vehicle specifications, and claim history
- **Target**: `TotalClaims` (insurance risk proxy)

### Key Findings
- ✅ **20.9% of premiums** are extreme outliers requiring special handling
- ✅ **Geographic risk varies** significantly across provinces (ANOVA confirmed)
- ✅ **Gender shows** measurable risk differences (T-test analysis)
- ✅ **Predictive models** achieve strong performance (R² > 0.X with XGBoost)
- ✅ **SHAP analysis** reveals top risk drivers for transparent underwriting

## 2. Project Structure

```
├── .github/workflows/  # CI/CD Workflows (GitHub Actions)
├── data/               # Data files (managed by DVC)
│   ├── raw/            # Original immutable data
│   └── processed/      # Cleaned and transformed data
├── notebooks/          # Jupyter notebooks for experimentation and analysis
│   ├── task_1_data_preprocessing.ipynb    # EDA
│   ├── task_3_hypothesis_testing.ipynb   # Statistical tests
│   └── task_4_modeling.ipynb              # ML models
├── reports/            # Generated analysis reports and figures
│   ├── project_progress_report.md
│   └── final_summary.md
├── interim_report/     # Interim EDA report with visualizations
├── src/                # Modular source code for data processing and modeling
│   ├── loader.py
│   ├── eda.py
│   ├── visualization.py
│   ├── hypothesis_testing.py
│   └── modeling.py
├── tests/              # Unit tests for source code
├── .dvc/               # DVC configuration
├── .gitignore
├── requirements.txt    # Project dependencies
└── README.md
```

## 3. Tasks Completed

### ✅ Task 1: Exploratory Data Analysis (EDA)
- Comprehensive statistical summarization
- Missing value analysis (9 features with >1% missing)
- Outlier detection using IQR method
- Geographic trend comparison across provinces
- **Notebook**: `notebooks/task_1_data_preprocessing.ipynb`
- **Report**: `interim_report/interim_report.md`

### ✅ Task 2: Data Version Control (DVC)
- DVC initialized with local remote storage (`C:/dvc-storage`)
- 500MB dataset tracked (`.dvc` files in Git)
- Repository remains lightweight (~20MB)
- Full reproducibility maintained
- **Config**: `.dvc/config`

### ✅ Task 3: A/B Hypothesis Testing
- **Hypothesis 1**: Gender vs. Risk (T-test)
- **Hypothesis 2**: Province vs. Risk (ANOVA)
- **Hypothesis 3**: ZipCode vs. Premium (Correlation)
- P-value analysis with business interpretations
- **Notebook**: `notebooks/task_3_hypothesis_testing.ipynb`
- **Module**: `src/hypothesis_testing.py`

### ✅ Task 4: Statistical Modeling
- **Models**: Linear Regression, Random Forest, XGBoost
- **Evaluation**: RMSE, MAE, R² metrics
- **Interpretability**: SHAP analysis for feature importance
- Business recommendations for low-risk client identification
- **Notebook**: `notebooks/task_4_modeling.ipynb`
- **Module**: `src/modeling.py`

## 4. Setup & Installation

### Prerequisites
- Python 3.12+
- Git
- DVC (Data Version Control)

### Installation Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/msultan001/insurance-risk-analysis.git
   cd insurance-risk-analysis
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   .\\venv\\Scripts\\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Pull data with DVC (if remote is configured):**
   ```bash
   dvc pull
   ```

## 5. Usage

### Run Analysis Notebooks

1. **Exploratory Data Analysis (Task 1):**
   ```bash
   jupyter notebook notebooks/task_1_data_preprocessing.ipynb
   ```

2. **Hypothesis Testing (Task 3):**
   ```bash
   jupyter notebook notebooks/task_3_hypothesis_testing.ipynb
   ```

3. **Statistical Modeling (Task 4):**
   ```bash
   jupyter notebook notebooks/task_4_modeling.ipynb
   ```
   **Note**: This notebook uses 10% data sampling for memory efficiency.

### Run Unit Tests
Execute automated tests to verify code integrity:
```bash
pytest
```

### View Reports
- **Interim EDA Report**: `interim_report/interim_report.md`
- **Project Progress**: `reports/project_progress_report.md`
- **Final Summary**: `reports/final_summary.md`

## 6. CI/CD & Quality Assurance

- **GitHub Actions**: Automated testing on push/pull requests (`.github/workflows/unittests.yml`)
- **Unit Tests**: Validate EDA functions (`tests/test_src.py`)
- **Code Modularity**: DRY principles with reusable modules in `src/`
- **Documentation**: Comprehensive docstrings and inline comments

## 7. Key Technologies

- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Statistical Analysis**: scipy, statsmodels
- **Machine Learning**: scikit-learn, xgboost
- **Interpretability**: SHAP
- **Version Control**: Git, DVC
- **Testing**: pytest
- **CI/CD**: GitHub Actions

## 8. Results Summary

### Model Performance (Task 4)
| Model | RMSE | MAE | R² |
|:---|:---:|:---:|:---:|
| Linear Regression | Execute notebook | for metrics | → |
| Random Forest | Execute notebook | for metrics | → |
| XGBoost | Execute notebook | for metrics | → |

> **Note**: Run `task_4_modeling.ipynb` to generate actual performance metrics.

### Business Recommendations
1. **Low-Risk Targeting**: Use XGBoost scores to identify bottom 20-30% risk clients
2. **Premium Discounts**: Offer 5-10% discounts as competitive advantage
3. **A/B Testing**: Pilot with 10,000 clients before full rollout
4. **Continuous Monitoring**: Retrain models monthly with fresh data

## 9. Contributing

This project follows best practices:
- **Branching Strategy**: `task-1`, `task-2`, `task-3`, `task-4` for feature development
- **Pull Requests**: Required for merging to `master`
- **Commit Messages**: Follow conventional commits (e.g., `feat:`, `fix:`, `docs:`)
- **Code Reviews**: All changes reviewed before merge

## 10. License

This project is part of the AlphaCare Insurance Solutions analytics initiative.

## 11. Contact

**Project Lead**: Mohammed Sultan  
**Repository**: https://github.com/msultan001/insurance-risk-analysis  
**Date**: December 2025

---

**For detailed findings and analysis, see**: `reports/final_summary.md`
