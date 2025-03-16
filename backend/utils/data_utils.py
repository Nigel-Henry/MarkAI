import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(data):
    """
    Analyze the given data and return a summary.

    Parameters:
    data (list or dict): The data to analyze.

    Returns:
    DataFrame: Summary statistics of the data.
    """
    df = pd.DataFrame(data)
    summary = df.describe()
    return summary

def plot_data(data):
    """
    Plot the given data and save it as a PNG file.

    Parameters:
    data (list or dict): The data to plot.

    Returns:
    str: The file path of the saved plot.
    """
    df = pd.DataFrame(data)
    df.plot(kind='bar')
    plt.savefig('plot.png')
    return 'plot.png'

def load_csv(file_path):
    """
    Load a CSV file into a DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: The loaded data.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return None

def filter_data(df, column, value):
    """
    Filter the DataFrame based on a column value.

    Parameters:
    df (DataFrame): The DataFrame to filter.
    column (str): The column to filter on.
    value: The value to filter by.

    Returns:
    DataFrame: The filtered data.
    """
    return df[df[column] == value]
