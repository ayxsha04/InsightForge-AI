import pandas as pd

def load_csv(uploaded_file):
    """
    Helper function to load a CSV file into a pandas DataFrame.
    
    Parameters:
        uploaded_file: The file-like object uploaded via Streamlit's file_uploader.
        
    Returns:
        pd.DataFrame: The loaded DataFrame if successful.
        
    Raises:
        ValueError: A clean, beginner-friendly error message if reading fails.
    """
    try:
        # Load the CSV file using pandas
        df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        # Raise a beginner-friendly ValueError with details about what failed
        raise ValueError(f"Could not read CSV file. Please make sure the file is formatted correctly. (Details: {e})")
