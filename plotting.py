# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 17:02:41 2023

@author: stozy1
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_graphs_h_original(base_filename, file_variants, file_conditions, all_data):
    """
    Generates a subplot for each condition and variant provided.

    Parameters:
        base_filename (str): The base filename before variant and condition.
        file_variants (list): A list of string variants to be used in filenames.
        file_conditions (list): A list of string conditions to be used in filenames.
        all_data (dict): All data
    """
    file_extension = '.csv'    

    sns.set_style("whitegrid")
    n_conditions = len(file_conditions)
    
    fig, axes = plt.subplots(nrows=n_conditions, ncols=1, figsize=(10, 6 * n_conditions))
    fig.tight_layout(pad=4.0)
    
    for idx, condition in enumerate(file_conditions):
        for variant in file_variants:
            filename = f"{base_filename}{variant}{condition}{file_extension}"
            key_name = f"{variant}{condition}"            
            
            if 'Time' in all_data[key_name].columns and 'Distance' in all_data[key_name].columns:
                axes[idx].scatter(all_data[key_name]['Time'], all_data[key_name]['Distance'], label=f"Q{condition}")
                
                avg_distance = all_data[key_name]['Distance'].mean()
                axes[idx].axhline(y=avg_distance, color='r', linestyle='--')
                axes[idx].text(0.5, avg_distance, f"Avg: {avg_distance:.4f}", color='r', va='center', ha='right', backgroundcolor='w')
                
            else:
                print(f"Columns 'Time' or 'Distance' not found in {filename}")

            axes[idx].set(title=f'Distance between Sensor to Water Surface (Q{condition})',
                          xlabel='Time',
                          ylabel='Distance')
            axes[idx].legend(title='Conditions', loc='upper left')
    
    plt.show()
    
def plot_graphs_h_MA(base_filename, file_variants, file_conditions, all_data):
    """
    Generates a subplot for each condition and variant provided.

    Parameters:
        base_filename (str): The base filename before variant and condition.
        file_variants (list): A list of string variants to be used in filenames.
        file_conditions (list): A list of string conditions to be used in filenames.
        all_data (dict): All data
    """
    file_extension = '.csv'    

    sns.set_style("whitegrid")
    n_conditions = len(file_conditions)
    
    fig, axes = plt.subplots(nrows=n_conditions, ncols=1, figsize=(10, 6 * n_conditions))
    fig.tight_layout(pad=4.0)
    
    for idx, condition in enumerate(file_conditions):
        for variant in file_variants:
            filename = f"{base_filename}{variant}{condition}{file_extension}"
            key_name = f"{variant}{condition}"            
            
            if 'Time' in all_data[key_name].columns and 'Distance_MA' in all_data[key_name].columns:
                axes[idx].plot(all_data[key_name]['Time'], all_data[key_name]['Distance_MA'], label=f"Q{condition}")
                
                avg_distance = all_data[key_name]['Distance_MA'].mean()
                axes[idx].axhline(y=avg_distance, color='r', linestyle='--')
                axes[idx].text(0.5, avg_distance, f"Avg: {avg_distance:.4f} [m]", color='r', va='center', ha='right', backgroundcolor='w')
                axes[idx].axhline(y=0.359, color='y', linestyle='--')
                axes[idx].text(0.5, 0.359, f"Distance b/w sensor to rocks: 0.359 [m]", color='r', va='center', ha='right', backgroundcolor='w')
                
            else:
                print(f"Columns 'Time' or 'Distance_MA' not found in {filename}")

            axes[idx].set(title=f'Distance between Sensor to Water Surface (Q{condition})',
                          xlabel='Time',
                          ylabel='Distance_MA')
            axes[idx].legend(title='Conditions', loc='upper right')
    
    plt.show()

def plot_graphs_h_depth(base_filename, file_variants, file_conditions, all_data):
    """
    Generates a subplot for each condition and variant provided.

    Parameters:
        base_filename (str): The base filename before variant and condition.
        file_variants (list): A list of string variants to be used in filenames.
        file_conditions (list): A list of string conditions to be used in filenames.
        all_data (dict): All data
    Returns:
        avg_distances (dict): A dictionary with average water depths for each variant and condition.
    """
    file_extension = '.csv'    

    sns.set_style("whitegrid")
    n_conditions = len(file_conditions)
    
    fig, axes = plt.subplots(nrows=n_conditions, ncols=1, figsize=(10, 6 * n_conditions))
    fig.tight_layout(pad=4.0)
    
    avg_distances = {}  # Dictionary to store average water depths
    
    for idx, condition in enumerate(file_conditions):
        for variant in file_variants:
            filename = f"{base_filename}{variant}{condition}{file_extension}"
            key_name = f"{variant}{condition}"            
            
            if 'Time' in all_data[key_name].columns and 'Water_depth' in all_data[key_name].columns:
                axes[idx].plot(all_data[key_name]['Time'], all_data[key_name]['Water_depth'], label=f"{variant}{condition}")
                
                avg_distance = all_data[key_name]['Water_depth'].mean()
                
                # Store the avg_distance in the dictionary
                avg_distances[key_name] = avg_distance
                
                axes[idx].axhline(y=avg_distance, color='r', linestyle='--')
                axes[idx].text(300, avg_distance, f"Avg: {avg_distance:.4f} [m]", color='r', va='center', ha='right', backgroundcolor='w')

            else:
                print(f"Columns 'Time' or 'Water_depth' not found in {filename}")

            axes[idx].set(title=f'Water depth at culvert outlet (Q{condition})',
                          xlabel='Time',
                          ylabel='Water_depth')
            axes[idx].legend(title='Conditions', loc='upper right')
    
    plt.show()  
    
    return avg_distances  # Returning the average distances dictionary
    

def plot_graphs_Q_original(base_filename, file_variants, file_conditions, all_data):
    """
    Generates a subplot for each condition and variant provided, focusing on Q values.

    Parameters:
        base_filename (str): The base filename before variant and condition.
        file_variants (list): A list of string variants to be used in filenames.
        file_conditions (list): A list of string conditions to be used in filenames.
        all_data (dict): All data
    """
    file_extension = '.csv'    

    sns.set_style("whitegrid")
    n_conditions = len(file_conditions)
    
    fig, axes = plt.subplots(nrows=n_conditions, ncols=1, figsize=(10, 6 * n_conditions))
    fig.tight_layout(pad=4.0)
    
    for idx, condition in enumerate(file_conditions):
        for variant in file_variants:
            filename = f"{base_filename}{variant}{condition}{file_extension}"
            key_name = f"{variant}{condition}"              
            
            # Check if 'Time' and 'Q' columns exist in the dataframe
            if 'Time' in all_data[key_name].columns and 'Discharge' in all_data[key_name].columns:
                # axes[idx].scatter(all_data[key_name]['Time'], all_data[key_name]['Discharge'], label=f"{variant}{condition}")
                axes[idx].scatter(range(len(all_data[key_name]['Discharge'])), all_data[key_name]['Discharge'], label=f"{variant}{condition}")                
                avg_Q = all_data[key_name]['Discharge'].mean()
                axes[idx].axhline(y=avg_Q, color='r', linestyle='--')
                axes[idx].text(0.5, avg_Q, f"Avg: {avg_Q:.4f}", color='r', va='center', ha='right', backgroundcolor='w')
                
            else:
                print(f"Columns 'Time' or 'Discharge' not found in {filename}")

            # Set axis labels and title
            axes[idx].set(title=f'Discharge Q Over Time ({variant}{condition})',
                          xlabel='Time Steps',
                          ylabel='Discharge Q')
            axes[idx].legend(title='Conditions', loc='upper left')
    
    # Display the plot
    plt.show()


def plot_graphs_Q_corrected(base_filename, file_variants, file_conditions, all_data):
    """
    Generates a subplot for each condition and variant provided, focusing on Q values.

    Parameters:
        base_filename (str): The base filename before variant and condition.
        file_variants (list): A list of string variants to be used in filenames.
        file_conditions (list): A list of string conditions to be used in filenames.
        all_data (dict): All data

    Returns:
        dict: A dictionary where keys are variant and condition strings, and values are respective average Q values.
    """
    file_extension = '.csv'    

    sns.set_style("whitegrid")
    n_conditions = len(file_conditions)
    
    fig, axes = plt.subplots(nrows=n_conditions, ncols=1, figsize=(10, 6 * n_conditions))
    fig.tight_layout(pad=4.0)

    # Dictionary to store the average Q values
    avg_Q_values = {}
    
    for idx, condition in enumerate(file_conditions):
        for variant in file_variants:
            filename = f"{base_filename}{variant}{condition}{file_extension}"
            key_name = f"{variant}{condition}"              
            
            # Check if 'Time' and 'Q' columns exist in the dataframe
            if 'Time' in all_data[key_name].columns and 'Discharge' in all_data[key_name].columns:
                # Define a mask to filter the data between x values 2000 and 4000
                time_steps = np.arange(len(all_data[key_name]['Discharge']))
                mask = (time_steps >= 2000) & (time_steps <= 4000)
                
                # Apply the mask to the data before plotting
                filtered_discharge = all_data[key_name]['Discharge'][mask]
                
                # Check if there is data left after filtering
                if not filtered_discharge.empty:
                    axes[idx].scatter(time_steps[mask], filtered_discharge, label=f"{variant}{condition}")                
                    avg_Q = filtered_discharge.mean()
                    axes[idx].axhline(y=avg_Q, color='r', linestyle='--')
                    axes[idx].text(2000.5, avg_Q, f"Avg: {avg_Q:.4f}", color='r', va='center', ha='right', backgroundcolor='w')
                    
                    # Store the average Q value in the dictionary
                    avg_Q_values[f"{variant}{condition}"] = avg_Q
                else:
                    print(f"No data left after filtering for {variant}{condition}. Skipping plot.")
                
            else:
                print(f"Columns 'Time' or 'Discharge' not found in {filename}")

            # Set axis labels and title
            axes[idx].set(title=f'Discharge Q Over Time ({variant}{condition})',
                          xlabel='Time Steps',
                          ylabel='Discharge Q')
            axes[idx].legend(title='Conditions', loc='upper left')
    
    # Display the plot
    plt.show()

    # Return the dictionary containing the average Q values
    return avg_Q_values
   

    
