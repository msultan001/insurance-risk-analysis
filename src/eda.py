
import pandas as pd
import numpy as np

def calculate_summary_statistics(df, columns=None):
    """
    Calculates summary statistics for numerical columns.
    Args:
        df (pd.DataFrame): Dataframe.
        columns (list): List of columns to analyze.
    Returns:
        pd.DataFrame: Summary statistics.
    """
    if columns:
        return df[columns].describe()
    return df.describe()

def check_missing_values(df):
    """
    Checks for missing values.
    Returns:
        pd.DataFrame: Count and percentage of missing values per column.
    """
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    missing_df = pd.DataFrame({'Missing Count': missing, 'Missing Percentage': missing_pct})
    return missing_df[missing_df['Missing Count'] > 0].sort_values(by='Missing Percentage', ascending=False)

def detect_outliers_iqr(df, column):
    """
    Detects outliers using IQR method.
    Args:
        df (pd.DataFrame): Dataframe.
        column (str): Column name.
    Returns:
        int: Number of outliers.
    """
    if column not in df.columns:
        return 0
    if not np.issubdtype(df[column].dtype, np.number):
        return 0
        
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return len(outliers)
