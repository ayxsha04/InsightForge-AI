import pandas as pd

def generate_profile(df):
    """
    Generates a simple dataset profiling report for a pandas DataFrame.
    This is the core analytics layer for InsightForge AI.
    """

    profile = {}

    # Basic structure info
    profile["row_count"] = df.shape[0]
    profile["column_count"] = df.shape[1]
    profile["column_names"] = list(df.columns)

    # Data types
    profile["data_types"] = df.dtypes.astype(str).to_dict()

    # Missing values
    profile["missing_values"] = df.isnull().sum().to_dict()

    # Duplicate rows
    profile["duplicate_rows"] = int(df.duplicated().sum())

    # Numeric summary
    profile["numeric_summary"] = df.describe().to_dict()

    return profile