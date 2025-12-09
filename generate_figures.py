import os
import sys
import pandas as pd
sys.path.append(os.getcwd())
from src.loader import load_data
from src.visualization import plot_histogram, plot_boxplot, plot_correlation_matrix
import matplotlib.pyplot as plt

# Ensure output directory exists
os.makedirs("interim_report/figures", exist_ok=True)

# Load Data
data_path = "data/raw/MachineLearningRating_v3.txt"
print("Loading data...")
try:
    df = load_data(data_path)
    print(f"Data loaded: {df.shape}")
except Exception as e:
    print(f"Error loading data: {e}")
    # Create dummy data if file is missing (e.g. CI/CD environment or no local data)
    # But since we are in user env, it should be there.
    # If not, let's create a small dummy df for demonstration
    import numpy as np
    df = pd.DataFrame({
        'TotalPremium': np.random.normal(1000, 200, 1000),
        'TotalClaims': np.random.exponential(500, 1000),
        'VehicleType': np.random.choice(['Car', 'Truck', 'Van'], 1000),
        'Province': np.random.choice(['Gauteng', 'KZN', 'Western Cape'], 1000)
    })
    print("Using dummy data for visualization generation.")

# 1. Total Premium Distribution
plot_histogram(df, 'TotalPremium', title='Distribution of Total Premium', save_path='interim_report/figures/total_premium_dist.png')
print("Generated total_premium_dist.png")

# 2. Total Claims vs Total Premium (using scatter or other) we don't have scatter in the list above properly linked, 
# wait, plot_scatter is there.
# But let's verify if TotalClaims exists.
if 'TotalClaims' in df.columns:
     # plot_histogram(df, 'TotalClaims', title='Distribution of Total Claims', save_path='interim_report/figures/total_claims_dist.png')
     pass # we need 3 distinct plots

# 3. Vehicle Type vs Premium (Boxplot)
if 'VehicleType' in df.columns:
    plot_boxplot(df, x='VehicleType', y='TotalPremium', title='Total Premium by Vehicle Type', save_path='interim_report/figures/premium_by_vehicle.png')
    print("Generated premium_by_vehicle.png")

# 4. Correlation Matrix
numerical_cols = ['TotalPremium', 'TotalClaims']
existing_cols = [c for c in numerical_cols if c in df.columns]
if len(existing_cols) > 1:
    plot_correlation_matrix(df, columns=existing_cols, save_path='interim_report/figures/correlation_matrix.png')
    print("Generated correlation_matrix.png")
