import pandas as pd
import csv


def log_results(csv_path, results_dict):
    """
    Log experiment results to a CSV file.
    ----------
    csv_path : [str] Path to the CSV file.
    results_dict : [dict] Dictionary containing the parameter names and results
    """
    # Convert the results dict to a single-row DataFrame
    new_entry = pd.DataFrame([results_dict]) 
    existing_df = pd.read_csv(csv_path)
    updated_df = pd.concat([existing_df, new_entry], ignore_index=True)
    updated_df.to_csv(csv_path, index=False)
    print(f'File updated: {csv_path}')
    

def save_as_csv(csv_file_path, data):
    # create new with or without contents (then data = [titles for each column])
    # Open the file in write mode
    with open(csv_file_path, mode='w', newline='') as file:
        # Create a csv.writer object
        writer = csv.writer(file)
        # Write data to the CSV file
        writer.writerows(data) # [[x] for x in data])
        # Print a confirmation message
        print(f"CSV file '{csv_file_path}' created successfully.")

"""
If want to create an empty csv for:
    
- data = [['Dataset', 'Accuracy',
          'Classical mean', 'Classical std',
        'Thermo (N=1) mean', 'Thermo (N=1) std',
        'Thermo (N=2) mean', 'Thermo (N=2) std',
        'Thermo (N=3) mean', 'Thermo (N=3) std',
        'Thermo (N=4) mean', 'Thermo (N=4) std',
        'Thermo (N=5) mean', 'Thermo (N=5) std',
        'Thermo (N=6) mean', 'Thermo (N=6) std',
        'Thermo (N=7) mean', 'Thermo (N=7) std',
        'Thermo (N=8) mean', 'Thermo (N=8) std',
        'Thermo (N=9) mean', 'Thermo (N=9) std',
        'Thermo (N=10) mean', 'Thermo (N=10) std']]
- summarise performance for method/redundancy
data = [['Dataset','Method','Avg Training Accuracy', 'Avg Testing Accuracy', 'Training/Test', 'Rules', 'Training loops']]
- summarise performance for specific redundancy to compare thermo. to class.
data = [['Dataset', 'Classical Accuracy', 'Thermodynamic Accuracy']]
"""
