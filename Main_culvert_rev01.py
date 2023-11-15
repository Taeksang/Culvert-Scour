# -*- coding: utf-8 -*-
"""
Script for data postprocessing of the Culvert Scour Experiment at the University of Michigan.

This script is designed to process the experimental data from the Culvert Scour Experiment.
It imports data from CSV files, processes discharge and water depth measurements, calculates
velocity, and computes the threshold velocities for different scour conditions.

Author: Taeksang Kim
Hydraulic Laboratory, University of Michigan

"""

import os
import numpy as np
import pandas as pd

# Custom modules
import csv_utils
import plotting

# Constants
BASE_FILENAME = 'Case07_'
FILE_EXTENSION = '.csv'
FILE_VARIANTS = ['h', 'Q']
FILE_CONDITIONS = ['50', '100', '150', '200', '250', '300']
PIPE_DIAMETER = 4
THRESHOLD_MULTIPLIER = 0.0254
CONVERSION_FACTOR_LPM_TO_CMS = 60000
CONVERSION_FACTOR_INCHES_TO_METERS = 39.3701
CONVERSION_FACTOR_FT_TO_M = 3.28084
SCALE_FACTOR = np.sqrt(12)

def import_data(variants, conditions, base_filename, file_extension):
    """
    Import experimental data from CSV files.

    Parameters:
    variants (list): List of different variants like water depth ('h') and discharge ('Q').
    conditions (list): Different experimental conditions like flow rates or time steps.
    base_filename (str): The base name of the CSV files.
    file_extension (str): The file extension, typically '.csv'.

    Returns:
    dict: A dictionary containing imported data indexed by variant and condition.
    """
    data = {}
    for variant in variants:
        for condition in conditions:
            filename = f"{base_filename}{variant}{condition}{file_extension}"
            key_name = f"{variant}{condition}"
            data[key_name] = csv_utils.import_csv_data(filename)
    return data

def process_discharge_data(data, conditions):
    """ Process discharge data and calculate average discharges. """
    avg_discharges = {}
    for condition in conditions:
        key_name = f"Q{condition}"
        data[key_name] = data[key_name][data[key_name]['Discharge'] != 0]
        avg_discharges[key_name] = data[key_name]['Discharge'].mean()
    return avg_discharges

def calculate_upward_velocity(measurements, time, conversion_factor):
    """ Calculate upward velocity from measurements. """
    return (np.array(measurements) / 2 / time / conversion_factor).tolist()

def calculate_area(h, R):
    """ Calculate area based on the water depth measurements h and radius R. """
    A = np.zeros(len(h))
    for i, depth in enumerate(h):
        if depth < R:
            theta = 2 * np.arccos((R - depth) / R)
            A[i] = R**2 * (theta - np.sin(theta))
        else:
            theta = 2 * np.arccos((depth - R) / R)
            A[i] = np.pi * R**2 - R**2 / 2 * (theta - np.sin(theta))
    return A

def print_threshold_velocities(velocities, ODOT, scale_factor):
    """ Print threshold velocities at prototype scale. """
    thresholds = {
        "First threshold Velocity, v1 (Start scour)": velocities[0],
        "Second threshold Velocity, v2 (Complete scour)": velocities[1],
        "Third threshold Velocity, v3 (RCP movement)": velocities[2]
    }

    for description, velocity in thresholds.items():
        print(f"< [Prototype Scale] {description} >", velocity * scale_factor, "ft/s")

    print("< [Prototype Scale] Threshold Velocity in ODOT chart (RCP movement) >", ODOT, "ft/s")

def main():
    """
    Main function that serves as the entry point of the program.
    
    It orchestrates the data import, processing, and analysis flow,
    and prints out the calculated results for further analysis.
    """
    # Import and process data
    all_data = import_data(FILE_VARIANTS, FILE_CONDITIONS, BASE_FILENAME, FILE_EXTENSION)
    plotting.plot_graphs_Q_original(BASE_FILENAME, ['Q'], FILE_CONDITIONS, all_data)
    
    avg_discharges = process_discharge_data(all_data, FILE_CONDITIONS)
    print("< Flume inlet Flowrate >", avg_discharges)
    
    # Convert dictionary values to NumPy arrays and perform division
    Q_inlet = np.array(list(avg_discharges.values())) / CONVERSION_FACTOR_LPM_TO_CMS
    
    # Calculate upward flowrate if pipe diameter is 1
    if PIPE_DIAMETER == 1:
        A_upward = 5 * 0.6
        v_upward = calculate_upward_velocity([19.5 - 16.1, 21.0 - 17.0, 22.1 - 17.0, 22.9 - 17.0, 24.2 - 18.5, 25.0 - 18.5], 300, CONVERSION_FACTOR_INCHES_TO_METERS)
        Q_upward = np.array(v_upward) * A_upward
        print("< Upward Flowrate >", Q_upward * CONVERSION_FACTOR_LPM_TO_CMS)
        Q = Q_inlet - Q_upward
    else:
        Q = Q_inlet

    print("< Flowrate at Culvert outlet >", Q * CONVERSION_FACTOR_LPM_TO_CMS)
    
    # Calculate cross-sectional area
    h = np.array([0.025, 0.037, 0.045, 0.05, 0.055, 0.06])  # Water depth by eye
    R = THRESHOLD_MULTIPLIER * PIPE_DIAMETER / 2
    A = calculate_area(h, R)
    
    # Calculate velocity
    v = Q / A * CONVERSION_FACTOR_FT_TO_M
    print("< [Model Scale] Velocity at Culvert outlet [Unit: ft/s] >", v)
    print("< [Prototype Scale] Velocity at Culvert outlet [Unit: ft/s] >", v * SCALE_FACTOR)
    
    # Print threshold velocities
    print_threshold_velocities(np.array([v[1],v[4],v[5]]), np.array(12), SCALE_FACTOR)


if __name__ == '__main__':
    main()
