
import pandas as pd
import os

def load_data(filepath):
    """
    Loads data from the specified filepath.
    Args:
        filepath (str): Path to the csv/txt file.
    Returns:
        pd.DataFrame: Loaded dataframe.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    # Attempt to read with different delimiters if needed, mostly | according to initial check, but notebook had \t
    # Based on the user notebook, it was checking MachineLearningRating_v3.txt, often these are pipe separated or tab
    # The notebook tried delimiter='\t'. I will try that first or |
    
    # Actually, let's peek at the file or assume the user knew it was tab separated?
    # Or make it robust.
    
    try:
        df = pd.read_csv(filepath, sep='|', low_memory=False) # Common for this dataset
        if df.shape[1] < 2:
             df = pd.read_csv(filepath, sep='\t', low_memory=False)
        if df.shape[1] < 2:
             df = pd.read_csv(filepath, sep=',', low_memory=False)
             
        # Check if dates need parsing, but keeping it simple for now.
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        raise e
