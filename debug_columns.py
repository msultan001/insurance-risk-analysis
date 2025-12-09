
import pandas as pd
import sys
import os

filepath = 'data/raw/MachineLearningRating_v3.txt'

try:
    print(f"Attempting to read {filepath} with separator '|'")
    df = pd.read_csv(filepath, sep='|', low_memory=False)
    if df.shape[1] < 2:
        print("Less than 2 columns found using '|', trying '\\t'")
        df = pd.read_csv(filepath, sep='\t', low_memory=False)
    if df.shape[1] < 2:
        print("Less than 2 columns found using '\\t', trying ','")
        df = pd.read_csv(filepath, sep=',', low_memory=False)
        
    print(f"Data loaded successfully. Shape: {df.shape}")
    print("Columns:")
    for col in df.columns:
        print(col)
except Exception as e:
    print(f"Error: {e}")
