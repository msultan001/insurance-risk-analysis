
import pandas as pd
from scipy import stats

def perform_t_test(df, group_col, value_col):
    """
    Performs a T-test to compare means of two groups.
    
    Args:
        df (pd.DataFrame): Dataframe containing the data.
        group_col (str): Column name for the grouping variable (must have 2 unique values).
        value_col (str): Column name for the numerical variable.
        
    Returns:
        dict: Test results including statistic, p-value, and interpretation.
    """
    groups = df[group_col].unique()
    if len(groups) != 2:
        return {"error": "T-test requires exactly two groups."}
        
    group1 = df[df[group_col] == groups[0]][value_col]
    group2 = df[df[group_col] == groups[1]][value_col]
    
    t_stat, p_val = stats.ttest_ind(group1, group2, nan_policy='omit')
    
    return {
        "test": "T-test",
        "statistic": t_stat,
        "p_value": p_val,
        "significant": p_val < 0.05,
        "interpretation": "Reject Null Hypothesis" if p_val < 0.05 else "Fail to Reject Null Hypothesis"
    }

def perform_chi2_test(df, col1, col2):
    """
    Performs a Chi-squared test of independence between two categorical variables.
    
    Args:
        df (pd.DataFrame): Dataframe containing the data.
        col1 (str): First categorical column.
        col2 (str): Second categorical column.
        
    Returns:
        dict: Test results including statistic, p-value, and interpretation.
    """
    contingency_table = pd.crosstab(df[col1], df[col2])
    chi2, p_val, dof, ex = stats.chi2_contingency(contingency_table)
    
    return {
        "test": "Chi-squared Test",
        "statistic": chi2,
        "p_value": p_val,
        "significant": p_val < 0.05,
        "interpretation": "Reject Null Hypothesis" if p_val < 0.05 else "Fail to Reject Null Hypothesis"
    }

def perform_anova(df, group_col, value_col):
    """
    Performs a one-way ANOVA test.
    """
    groups = [group[value_col].dropna() for name, group in df.groupby(group_col)]
    f_stat, p_val = stats.f_oneway(*groups)
    
    return {
        "test": "ANOVA",
        "statistic": f_stat,
        "p_value": p_val,
        "significant": p_val < 0.05,
        "interpretation": "Reject Null Hypothesis" if p_val < 0.05 else "Fail to Reject Null Hypothesis"
    }
