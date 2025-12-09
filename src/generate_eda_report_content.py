import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Add project root to path
sys.path.append(os.getcwd())

from src.loader import load_data
from src.eda import calculate_summary_statistics, check_missing_values, detect_outliers_iqr

def generate_eda_content():
    # Load Data
    data_path = "data/raw/MachineLearningRating_v3.txt"
    try:
        df = load_data(data_path)
        print(f"Data loaded successfully: {df.shape}")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # 1. Descriptive Statistics
    print("\n--- Descriptive Statistics ---")
    numerical_cols = ['TotalPremium', 'TotalClaims']
    # Filter for numerical columns that exist
    available_cols = [c for c in numerical_cols if c in df.columns]
    if available_cols:
        stats = calculate_summary_statistics(df, columns=available_cols)
        print(stats.to_markdown())
    else:
        print("No numerical columns found for stats.")

    # 2. Missing Values
    print("\n--- Missing Values Analysis ---")
    missing_df = check_missing_values(df)
    if not missing_df.empty:
        print(missing_df.to_markdown())
    else:
        print("No missing values found.")

    # 3. Outlier Analysis
    print("\n--- Outlier Analysis ---")
    for col in available_cols:
        outlier_count = detect_outliers_iqr(df, col)
        percentage = (outlier_count / len(df)) * 100
        print(f"Column: {col} | Outliers: {outlier_count} | Percentage: {percentage:.2f}%")

    # 4. Geographic Trends
    print("\n--- Generating Geographic Trend Plots ---")
    os.makedirs("interim_report/figures", exist_ok=True)
    
    if 'Province' in df.columns and 'TotalPremium' in df.columns:
        plt.figure(figsize=(10, 6))
        province_premium = df.groupby('Province')['TotalPremium'].mean().sort_values()
        sns.barplot(x=province_premium.index, y=province_premium.values, palette="viridis")
        plt.title('Average Total Premium by Province')
        plt.ylabel('Average Total Premium')
        plt.xlabel('Province')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('interim_report/figures/avg_premium_by_province.png')
        print("Saved interim_report/figures/avg_premium_by_province.png")
        plt.close()

    if 'Province' in df.columns and 'TotalClaims' in df.columns:
        plt.figure(figsize=(10, 6))
        province_claims = df.groupby('Province')['TotalClaims'].mean().sort_values()
        sns.barplot(x=province_claims.index, y=province_claims.values, palette="magma")
        plt.title('Average Total Claims by Province')
        plt.ylabel('Average Total Claims')
        plt.xlabel('Province')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('interim_report/figures/avg_claims_by_province.png')
        print("Saved interim_report/figures/avg_claims_by_province.png")
        plt.close()

if __name__ == "__main__":
    generate_eda_content()
