'''
***
This code is designed to analyze and visualize contrast sensitivity responses (CSRs) from multiple experiments by processing and aggregating results from several JSON files.

How to use this code:

Store all output Json files in a folders (e.g., a group of experiments with specified experimental configurations)

Run the Script: Execute the python script. Input and output directories will be defined in pop-up windows. 

Interpret the Results: The script will generate a figure per measured position. In each plot, the mean and standard deviation of the CSR will be visualized.  

X-axis: Spatial Frequency (cycles/degree)

Y-axis: CSR on a logarithmic scale. Each plot represents a different position in the visual field.

The line in each plot shows the average contrast sensitivity across all processed files for that position.
***
'''

# Import nessecary dependencies for python code below
import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Input the directory with the json files
def get_directory_path():
    # Create a root window but hide it
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a directory dialog and let the user select a directory
    directory_path = filedialog.askdirectory(title="Select a Directory")
    
    return directory_path

# Call the function and print the selected directory path
folder_path = get_directory_path()
print(f"Selected directory: {folder_path}")

# Output file name and path
def get_output_file():
    """Function to prompt the user to select an output file name using tkinter's Save As dialog."""
    # Create the root window, but hide it (we don't need a visible window)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a "Save As" dialog and return the selected file path
    file_path = filedialog.asksaveasfilename(
        title="Save the output file",  # Title of the dialog window
        defaultextension=".png",  # Default extension (set to .png)
        filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")],  # File types filter
    )

    return file_path
# Call the function and print the selected output directory path
output_file = get_output_file()
if output_file:
    print(f"Output file selected: {output_file}")
else:
    print("No file selected.")

# Plot contrast sensitivity graphs
def openFile(path):
    with open(path, 'r') as f:
        return json.loads(f.read())

def reorder(df_nested_list):

    # Convert position to string and then check for unique values
    positions = df_nested_list['position'].astype(str).unique()

    # If more than one position, drop the first row
    if len(positions) > 1:
        df_nested_list = df_nested_list.iloc[1:].reset_index(drop=True)


    n = len(df_nested_list)
    for index, row in df_nested_list.iterrows():
        if (index-1)%9 == 0 and index+4 < n:
            center = df_nested_list.loc[index].values
            df_nested_list.loc[index] = df_nested_list.loc[index+1].values
            df_nested_list.loc[index+1] = df_nested_list.loc[index+2].values
            df_nested_list.loc[index+2] = df_nested_list.loc[index+3].values
            df_nested_list.loc[index+3] = df_nested_list.loc[index+4].values
            df_nested_list.loc[index+4] = center
    return df_nested_list

def process_file(file_path):
    data = openFile(file_path)
    df_nested_list = pd.json_normalize(data, record_path=['responses'])
    df_nested_list = reorder(df_nested_list)

    df_combined = df_nested_list[["frequency", "position", "contrast"]].copy()
    df_combined.loc[:, 'position'] = df_combined["position"].map(str)
    df_combined.loc[:, 'frequency'] = df_combined['frequency'].map(float)
    df_combined.loc[:, 'contrast'] = df_combined['contrast'].map(float)
    df_combined.loc[:, 'contrast'] = 1 / df_combined['contrast']

    return df_combined

def plot_results(df_combined):
    positions = df_combined['position'].unique()
    num_positions = len(positions)

    # Determine the grid size based on the number of positions
    if num_positions <= 1:
        fig, ax = plt.subplots(1, 1, figsize=(8, 6))
        axes = [ax]
    else:
        rows = int(np.ceil(np.sqrt(num_positions)))
        cols = int(np.ceil(num_positions / rows))
        fig, axes = plt.subplots(rows, cols, figsize=(6*cols, 4*rows))
        axes = axes.flatten()

    for i, position in enumerate(positions):
        ax = axes[i]
        subset = df_combined[df_combined['position'] == position]

        # Group by frequency and calculate mean, std, and standard error
        stats = subset.groupby('frequency')['contrast'].agg(['mean', 'std', 'count'])
        stats['stderr'] = stats['std'] / np.sqrt(stats['count'])

        # Check if there's more than one data point per frequency
        multiple_data_points = (stats['count'] > 1).any()

        if not stats.empty and not stats['std'].isnull().all() and multiple_data_points:
            # Plot with error bars for standard deviation and standard error
            ax.errorbar(stats.index, stats['mean'], yerr=stats['std'], fmt='o-', label='Mean ± Std Dev')
            #ax.errorbar(stats.index, stats['mean'], yerr=stats['stderr'], fmt='o-', label='Mean ± Std Error', color='gray')
            #ax.errorbar(stats.index, stats['mean'], yerr=stats['stderr'], fmt='o-', label='Mean ± Std Error', linestyle='--', color='gray')
        else:
            # Plot without error bars if no variation in data
            ax.plot(stats.index, stats['mean'], 'o-', label='Mean')

        ax.set_xlabel('Spatial Frequency (cycles/degree)')
        ax.set_ylabel('Contrast Sensitivity Function (CSF)')
        ax.set_yscale('log')
        ax.set_ylim(0.5, 200)
        ax.set_title(f'Position {position}')
        ax.grid(True)
        ax.legend()

    # Remove any unused subplots
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    return plt.gcf()
    
    #plt.show()

# Main execution
all_dfs = []

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        df = process_file(file_path)
        all_dfs.append(df)

        
# Concatenate all dataframes
df_combined = pd.concat(all_dfs, ignore_index=True)

# Check if df_combined is empty
if df_combined.empty:
    print("Error: Combined dataframe is empty. Please check the input data.")
else:
    # Plot the results and get the figure
    fig = plot_results(df_combined)

    # Check if fig is None (for debugging)
    if fig is None:
        print("Error: plot_results returned None, the figure was not created.")
    else:
        # Specify the filename for saving the figure
        jpeg_filename = output_file

        # Save the figure to the specified file
        fig.savefig(jpeg_filename, format='png')

        # Close the figure to free up memory
        plt.close(fig)

        print(f"Plot has been saved as {jpeg_filename}")
