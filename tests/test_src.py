
import pytest
import pandas as pd
import numpy as np
import sys
import os

# Ensure src is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.eda import calculate_summary_statistics, check_missing_values, detect_outliers_iqr

def test_calculate_summary_statistics():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]})
    stats = calculate_summary_statistics(df, ['A'])
    assert 'A' in stats.columns
    assert stats.loc['mean', 'A'] == 3.0

def test_check_missing_values():
    df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, None]})
    missing = check_missing_values(df)
    assert missing.loc['B', 'Missing Count'] == 2
    assert missing.loc['A', 'Missing Count'] == 1

def test_detect_outliers_iqr():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 100]}) # 100 is an outlier
    outliers = detect_outliers_iqr(df, 'A')
    assert outliers == 1
    
    df_no_outlier = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
    outliers_none = detect_outliers_iqr(df_no_outlier, 'A')
    assert outliers_none == 0
