
import pandas as pd
import os

def load_data(filepath):
    """
    Loads data from the specified filepath with proper encoding detection.
    Args:
        filepath (str): Path to the csv/txt file.
    Returns:
        pd.DataFrame: Loaded dataframe.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    # Try different encodings and separators
    # The file appears to be UTF-16 LE encoded with pipe separator
    encodings = ['utf-16-le', 'utf-16', 'utf-8', 'latin1']
    separators = ['|', '\t', ',']
    
    for encoding in encodings:
        for sep in separators:
            try:
                df = pd.read_csv(
                    filepath, 
                    sep=sep, 
                    encoding=encoding,
                    low_memory=False,
                    on_bad_lines='skip'  # Skip problematic lines
                )
                # Check if we got a valid dataframe with multiple columns
                if df.shape[1] >= 2:
                    print(f"Successfully loaded data with encoding={encoding}, separator='{sep}'")
                    return df
            except Exception:
                continue
    
    # If all attempts fail, raise an error
    raise ValueError(f"Could not load data from {filepath} with any supported encoding/separator combination")
