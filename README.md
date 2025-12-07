# Insurance Risk & Predictive Analytics Project

## 1. Project Background
**AlphaCare Insurance Solutions (ACIS)** is at the forefront of risk and predictive analytics in South Africa's car insurance marketing sector. This project focuses on analyzing historical insurance claim data to optimize marketing strategies and identify "low-risk" customer segments. The ultimate discovery of these segments will allow for premium reductions, thereby attracting new clients and enhancing market competitiveness.

## 2. Key Objectives
- **Exploratory Data Analysis (EDA):** Analyze historical claim data to understand distributions, correlations, and potential risk factors.
- **Risk Segmentation:** Identify low-risk targets for potential premium optimization.
- **Marketing Optimization:** Provide data-driven insights to refine marketing strategies.
- **Statistical Modeling (Future Scope):** Develop predictive models for claim probability and risk assessment.

## 3. Project Structure
The repository is organized as follows:

```
├── .github/workflows/  # CI/CD Workflows (GitHub Actions)
├── data/               # Data files (managed by DVC)
│   ├── raw/            # Original immutable data
│   └── processed/      # Cleaned and transformed data
├── docs/               # Project documentation
├── notebooks/          # Jupyter notebooks for experimentation and analysis
├── reports/            # Generated analysis reports and figures
├── src/                # Modular source code for data processing and modeling
├── tests/              # Unit tests for source code
├── .dvc/               # DVC configuration
└── requirements.txt    # Project dependencies
```

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
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 5. Data Version Control (DVC)
This project uses DVC to manage large datasets. To fetch the data:
1. Ensure you have access to the remote storage (if configured).
2. Pull the data:
   ```bash
   dvc pull
   ```

## 6. Usage
- **Exploratory Data Analysis:**
  Navigate to `notebooks/` and run `task_1_data_preprocessing.ipynb` to see the initial data analysis and visualization.
  ```bash
  jupyter notebook notebooks/task_1_data_preprocessing.ipynb
  ```

- **Running Tests:**
  Execute unit tests to verify the integrity of the source code.
  ```bash
  pytest
  ```


