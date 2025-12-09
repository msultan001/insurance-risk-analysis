
import pandas as pd
import numpy as np
import shap
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler,  LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

class DataPreprocessor:
    def __init__(self, categorical_features, numerical_features):
        self.categorical_features = categorical_features
        self.numerical_features = numerical_features
        
        # Define preprocessing pipelines
        self.numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])
        
        self.categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
        ])
        
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', self.numeric_transformer, self.numerical_features),
                ('cat', self.categorical_transformer, self.categorical_features)
            ])
            
    def fit_transform(self, X):
        return self.preprocessor.fit_transform(X)
        
    def transform(self, X):
        return self.preprocessor.transform(X)

    def get_feature_names(self):
        """Extract feature names after transformation."""
        feature_names = list(self.numerical_features)
        
        try:
            cat_encoder = self.preprocessor.named_transformers_['cat'].named_steps['encoder']
            if hasattr(cat_encoder, 'get_feature_names_out'):
                feature_names.extend(cat_encoder.get_feature_names_out(self.categorical_features))
        except Exception as e:
            print(f"Warning: Could not extract specific feature names: {e}")
             
        return feature_names

def train_linear_regression(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def train_random_forest(X_train, y_train, n_estimators=100, random_state=42):
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)
    model.fit(X_train, y_train)
    return model

def train_xgboost(X_train, y_train, random_state=42):
    model = XGBRegressor(objective='reg:squarederror', random_state=random_state)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    return {
        "RMSE": rmse,
        "MAE": mae,
        "R2": r2
    }

def explain_model_shap(model, X_sample):
    """
    Generates SHAP values for a given model and sample data.
    """
    explainer = shap.Explainer(model)
    shap_values = explainer(X_sample)
    return shap_values
