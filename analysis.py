import matplotlib.pyplot as plt
import zipfile
import numpy as np
import pandas as pd
import csv


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
    
- 
data = [['Dataset', 'Accuracy',
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

def compile_results(dataset, accuracy_column, accuracy_type): 
    """
    calculate mean/stdev for each dataset for training/testing for each 
    technique (classical/thermodynamic+redundancy) and save to summary csv
    ----------
    dataset: [str] name of dataset 
    (choose from: 'mushroom', 'breast_cancer', 'spam', 'tictactoe', 'income')
    accuracy_column: [str] testing/training accuracy
    (choose from: 'Avg Testing Accuracy', 'Avg Training Accuracy')
    accuracy_type: either 'testing' or 'training'
   """
    df = pd.read_csv(f"{dataset}_performance.csv")
    values = (df.groupby('Method')[f'{accuracy_column}']
              .agg(["mean", "std"])
              .stack(level=0).to_frame().T)
    values = values.to_numpy()

    stats = np.zeros(22)
    for i in range(values.shape[1]):
        stats[i] = values[0,i]

    results_dict = {'Dataset': dataset, 'Accuracy': accuracy_type,
               'Classical mean': stats[0], 'Classical std': stats[1],
               'Thermo (N=1) mean': stats[2], 'Thermo (N=1) std': stats[3],
               'Thermo (N=2) mean': stats[4], 'Thermo (N=2) std': stats[5],
               'Thermo (N=3) mean': stats[6], 'Thermo (N=3) std': stats[7],
               'Thermo (N=4) mean': stats[8], 'Thermo (N=4) std': stats[9],
               'Thermo (N=5) mean': stats[10], 'Thermo (N=5) std': stats[11],
               'Thermo (N=6) mean': stats[12], 'Thermo (N=6) std': stats[13],
               'Thermo (N=7) mean': stats[14], 'Thermo (N=7) std': stats[15],
               'Thermo (N=8) mean': stats[16], 'Thermo (N=8) std': stats[17],
               'Thermo (N=9) mean': stats[18], 'Thermo (N=9) std': stats[19],
               'Thermo (N=10) mean': stats[20], 'Thermo (N=10) std': stats[21]}
    log_results('results/summary.csv', results_dict)

def get_stats(dataset_choice, df):
    """
    produces statistics for performance for a given dataset
    calculates average and standard deviation for training and testing performance 
    for each method (i.e., classical, thermodynamic + redundancy) for each dataset
    ----------
    dataset_choice: [str] name of dataset
    (choose from: 'mushroom', 'breast_cancer', 'spam', 'tictactoe', 'income')
    df: [dataframe] performance values (from summary.csv)
    """
    dataset = df[df['Dataset'] == dataset_choice]
    labels = ['Classical', 'N=1', 'N=2', 'N=3', 'N=4', 'N=5']

    training = dataset[dataset['Accuracy'] == 'training']
    training_mean = training.loc[:, training.columns.str.contains("mean")].iloc[:, :6]
    training_std  = training.loc[:, training.columns.str.contains("std")].iloc[:, :6]
    training_mean = training_mean.apply(pd.to_numeric)
    training_std  = training_std.apply(pd.to_numeric)
    
    testing = dataset[dataset['Accuracy'] == 'testing']
    testing_mean = testing.loc[:, testing.columns.str.contains("mean")].iloc[:, :6]
    testing_std  = testing.loc[:, testing.columns.str.contains("std")].iloc[:, :6]
    testing_mean = testing_mean.apply(pd.to_numeric)
    testing_std  = testing_std.apply(pd.to_numeric)
    return training_mean, training_std, testing_mean, testing_std, labels


def generate_table(dataset_choice, df):
    """
    generate a performance table for a given dataset
    ----------
    dataset_choice: [str] name of dataset
    (choose from: 'mushroom', 'breast_cancer', 'spam', 'tictactoe', 'income')
    df: [dataframe] performance values (from summary.csv)
    """
    
    training_mean, training_std, testing_mean, testing_std, labels = get_stats(dataset_choice, df)
    training_avg = training_mean.iloc[0].to_numpy()
    training_err = training_std.iloc[0].to_numpy()
    
    testing_avg = testing_mean.iloc[0].to_numpy()
    testing_err = testing_std.iloc[0].to_numpy()
    
    # Format as mean ± std
    training_pm = [f"{m:.1f} ± {s:.1f}" for m, s in zip(training_avg, training_err)]
    testing_pm  = [f"{m:.1f} ± {s:.1f}" for m, s in zip(testing_avg, testing_err)]

    results_df = pd.DataFrame({
        'Training Accuracy': training_pm,
        'Testing Accuracy': testing_pm
        }, index=labels)
    
    print(results_df)
    return results_df

def print_performance_tables():
    """
    print performance averages/errors for each dataset.
    """
    datasets = ['breast_cancer', 'income', 'mushroom', 'spam', 'tictactoe']
    df = pd.read_csv('summary.csv')
    for dataset_choice in datasets:
        print(f'Dataset: {dataset_choice}')
        generate_table(dataset_choice, df)
        
def complete_summary_table():
    """
    Output a condensd summary of performance for each dataset
    Classical/Thermal (N=3)
    """
    datasets = ['breast_cancer', 'income', 'mushroom', 'spam', 'tictactoe']
    df = pd.read_csv('summary.csv')
    
    summary_table = []
    for dataset_choice in datasets:
        dataset = df[df['Dataset'] == dataset_choice]
        testing = dataset[dataset['Accuracy'] == 'testing']
        classical_mean = testing.loc[:, testing.columns.str.contains
                                     ("Classical mean", regex=False)].apply(pd.to_numeric).iloc[0, 0]
        classical_std  = testing.loc[:, testing.columns.str.contains
                                     ("Classical std", regex=False)].apply(pd.to_numeric).iloc[0, 0]
        thermal_mean = testing.loc[:, testing.columns.str.contains
                                   ("Thermo (N=3) mean", regex=False)].apply(pd.to_numeric).iloc[0, 0]
        thermal_std  = testing.loc[:, testing.columns.str.contains
                                   ("Thermo (N=3) std", regex=False)].apply(pd.to_numeric).iloc[0, 0]

        classical_pm = f"{classical_mean:.1f} ± {classical_std:.1f}"
        thermal_pm = f"{thermal_mean:.1f} ± {thermal_std:.1f}"

        results_dict = {'Dataset': dataset_choice, 'Classical Accuracy': classical_pm, 'Thermodynamic Accuracy': thermal_pm}
        summary_table.append(results_dict)

    summary_stats = pd.DataFrame(summary_table)
    print(summary_stats)
    return summary_stats

# =============================================================================

# loop through all dataset to compile performance averages to summary.csv
datasets = ['tictactoe', 'breast_cancer', 'income', 'mushroom',
            'spam'] 
# for dataset in datasets:
  #   compile_results(dataset, 'Avg Testing Accuracy', 'testing')
    # compile_results(dataset, 'Avg Training Accuracy', 'training')        

# now, produce a summary table for each dataset and a condensed summary
# with just testing accuracy for classical and thermodynamic(N=3)
# complete_summary_table() 
# print_performance_tables()     
