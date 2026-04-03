# Interpretable-rule-based-learning-with-thermodynamic-neurons
This contains the code to reproduce the results of 'Interpretable Rule-Based Learning with Thermodynamic Neurons.'
In [src](src):<br>
* [network_with_signal](network_with_signal.ipynb) includes: <br>
**simulated NOT, AND, OR gates
** plot of excited population of signal qubit coupled to a NOT gate as a function of thermalisation time (T)
** simulation of thermodynamic single-feature network
** probability tables for: False positive vs False negative for each gate at $T=50$, probability of correct output for each gate and the signal-feature network as a function of thermalisation time ($T$)
* [plot_gate_behaviour](plot_gate_behaviour.ipynb) includes:<br>
** plot of virtual temperature $\beta_v$ of three-qubit machine as a function of $\beta_1$ (temperature inversion)
** plot of sigmoid vs steady state temperature $\beta_z^\infty$ of NOT gate as a function of $\beta_1$
** plot of steady state output $\beta_v^\infty$ for NOT gate for varying $\epsilon_1$
** plot of steady state output temperature $\beta_v^\infty$ for AND gate as a function of $\beta_1,\beta_2$
** plot of steady state output temperature $\beta_v^\infty$ for OR gate as a function of $\beta_1,\beta_2$

*[cat_bird_classifier](cat_bird_classifier.py) <br>
used as as an example use of Tsetlin machine algorithm (classical or thermodynamic) for classification of inputs (either cat or bird). Plots final memory states for cat rule and prints explicit logical rule for cat and bird.

*[data_classifier](data_classifier.py) <br>
used to test classical/thermodynamic classifier, returns training and testing accuracy. Can store results in a csv.
*[analysis](analysis.py)<br>
used to produce performance tables for [individual datasets]

  
In [results](results): <br>
data collected which leads to the tables of classification accuracy for different datasets ([breast cancer](results/breast_cancer_performance.csv), [mushroom](results/mushroom_performance.csv), [tic-tac-toe](results/tictactoe_performance.csv), [income](results/income_performance.csv), [spam](results/spam_performance.csv)) as well as a condensed summary of [average performance](results/summary.csv), which appear in the results and appendix.

* [Tsetlin_machine_framework](src/Tsetlin_machine_framework.py) - uses Memory class to keep record of and update memory states during learning in order to produce a rule. Use [this](https://github.com/sparrowsuderman/Interpretable-rule-based-learning-with-thermodynamic-neurons/blob/b264d8364b1e815cb4a3d78410edc2f41780383b/src/Tsetlin_machine_framework.py#L29) function.

* analysis - used to produce data summary tables shown in results/appendix, ind averages and standard deviations for each dataset and training/testing and compile into summary.csv
  
  * now we want to produce a summary table for each dataset and a summary for the whole thing where we restrict to testing accuracy for classical and thermodynamic N=3
    
binarizer - used to booleanize continuous features in dataset
cat_bird_classifier - example use of Tsetlin machine on simple dataset - produce graph of memory states and states explicit rules
data_classifier - use to test classifier on datasets featured in results section. from here you can choose the dataset and classification method (+ redundancy), obtain the performance accuracy and save it to a csv if desired.
data_prep - fetch, prepare and sort data for classification
results - to contain: income_performance.csv, spam_performance.csv, tictactoe_performance.csv, mushroom_performance.csv, breast_cancer_performance.csv

network - uses gates to determine output of thermodynamic 'Rule-evaluation engine'
thermal gates - probabilistic model for thermodynamics gates to obtain fast outputs for classification rather than full simulation of dynamics
store_results - log performance results to csv, creat new csv files
