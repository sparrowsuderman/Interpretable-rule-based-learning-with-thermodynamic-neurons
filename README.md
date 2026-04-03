# Interpretable-rule-based-learning-with-thermodynamic-neurons
This contains the code to reproduce the results of my MSci thesis titled 'Interpretable Rule-Based Learning with Thermodynamic Neurons.'

Tsetlin_machine_framework
data_classifier - from here you can choose the dataset and classification method (+ redundancy), obtain the performance accuracy and save it to a csv if desired.
-> analysis_data_handling - prep_data (fetch, prepare and sort data for classification)
- log_results (save performance results to a csv
-> Tsetlin_machine_framework  - uses Memory class to keep record of and update memory states in order to produce a rule.

cat_bird_classifier - basic example - prints rules explicitly and plots corresponding memory states 

thermal_gates - probabilistic model for gates to obtain fast outputs for classification

network - uses gates to determine output of thermodynamic 'Rule-evaluation engine'

binarizer - used to booleanize continuous data

To analyse results:
- save performance of each dataset to a unique csv file  in folder called results (i.e., breast_cancer_performance.csv) 
start with: income_performance.csv, spam_performance.csv, tictactoe_performance.csv, mushroom_performance.csv, breast_cancer_performance.csv

- then find averages and standard deviations for each dataset and training/testing and compile into summary.csv
- now we want to produce a summary table for each dataset and a summary for the whole thing where we restrict to testing accuracy for classical and thermodynamic N=3
