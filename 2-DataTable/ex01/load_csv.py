import pandas as pd
import os

def load(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file from the given path and return it as a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The data from the CSV file as a DataFrame.
    
    Raises:
        ValueError: If the file cannot be loaded or does not exist.

    """
    if not os.path.exists(file_path):
        raise ValueError(f"File not found: {file_path}")
    if not file_path.endswith('.csv'):
        raise ValueError(f"File is not a CSV: {file_path}")
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise ValueError(f"Could not load CSV file: {e}") from e