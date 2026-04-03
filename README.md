# Interpretable-rule-based-learning-with-thermodynamic-neurons
This contains the code to reproduce the results of my MSci thesis titled 'Interpretable Rule-Based Learning with Thermodynamic Neurons.'

[Tsetlin_machine_framework](src/Tsetlin_machine_framework.py) - uses Memory class to keep record of and update memory states during learning in order to produce a rule.
analysis - used to produce data summary tables shown in results/appendix, ind averages and standard deviations for each dataset and training/testing and compile into summary.csv
- now we want to produce a summary table for each dataset and a summary for the whole thing where we restrict to testing accuracy for classical and thermodynamic N=3
binarizer - used to booleanize continuous features in dataset
cat_bird_classifier - example use of Tsetlin machine on simple dataset - produce graph of memory states and states explicit rules
data_classifier - use to test classifier on datasets featured in results section. from here you can choose the dataset and classification method (+ redundancy), obtain the performance accuracy and save it to a csv if desired.
data_prep - fetch, prepare and sort data for classification
results - to contain: income_performance.csv, spam_performance.csv, tictactoe_performance.csv, mushroom_performance.csv, breast_cancer_performance.csv

network - uses gates to determine output of thermodynamic 'Rule-evaluation engine'
thermal gates - probabilistic model for thermodynamics gates to obtain fast outputs for classification rather than full simulation of dynamics
store_results - log performance results to csv, creat new csv files
