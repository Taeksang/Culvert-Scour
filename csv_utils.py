# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08

@author: Taeksang Kim _ University of Michigan _ Hydraulic Laboratory
"""
import pandas as pd

def import_csv_data(filename):
    """
    Import CSV data.

    Parameters:
        filename (str): The name of the CSV file.

    Returns:
        pd.DataFrame: The data imported from the CSV file.
    """
    try:
        data = pd.read_csv(filename, error_bad_lines=False, warn_bad_lines=True)
        return data
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


