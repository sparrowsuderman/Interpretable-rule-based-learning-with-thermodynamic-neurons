# Interpretable-rule-based-learning-with-thermodynamic-neurons
This contains the code to reproduce the results of 'Interpretable Rule-Based Learning with Thermodynamic Neurons.'<br>
In [src/](src):<br>
* [network_with_signal](network_with_signal.ipynb) includes: <br>
  - simulated NOT, AND, OR gates
  - plot of excited population of signal qubit coupled to a NOT gate as a function of thermalisation time (T)
  - simulation of thermodynamic single-feature network
  - probability tables for: False positive vs False negative for each gate at $T=50$, probability of correct output for each gate and the signal-feature network as a function of thermalisation time ($T$)
* [plot_gate_behaviour](plot_gate_behaviour.ipynb) includes:<br>
  - plot of virtual temperature $\beta_v$ of three-qubit machine as a function of $\beta_1$ (temperature inversion)
  - plot of sigmoid vs steady state temperature $\beta_z^\infty$ of NOT gate as a function of $\beta_1$
  - plot of steady state output $\beta_v^\infty$ for NOT gate for varying $\epsilon_1$
  - plot of steady state output temperature $\beta_v^\infty$ for AND gate as a function of $\beta_1,\beta_2$
  - plot of steady state output temperature $\beta_v^\infty$ for OR gate as a function of $\beta_1,\beta_2$

* [cat_bird_classifier](cat_bird_classifier.py) <br>
used as as an example use of Tsetlin machine algorithm (classical or thermodynamic) for classification of inputs (either cat or bird). Plots final memory states for cat rule and prints explicit logical rule for cat and bird.

* [data_classifier](data_classifier.py) <br>
used to test classical/thermodynamic classifier, returns training and testing accuracy. Can store results in a csv.
*[analysis](analysis.py)<br>
used to produce performance tables for [individual datasets](https://github.com/sparrowsuderman/Interpretable-rule-based-learning-with-thermodynamic-neurons/blob/5cc6e40a11e724332872d5766309db87b054acaf/src/analysis.py#L184), [condensed summary](https://github.com/sparrowsuderman/Interpretable-rule-based-learning-with-thermodynamic-neurons/blob/5cc6e40a11e724332872d5766309db87b054acaf/src/analysis.py#L183) table of testing classical and thermodynamic ($N=3$) accuracy for each dataset

  
In [results/](results): <br>
data collected which leads to the tables of classification accuracy for different datasets ([breast cancer](results/breast_cancer_performance.csv), [mushroom](results/mushroom_performance.csv), [tic-tac-toe](results/tictactoe_performance.csv), [income](results/income_performance.csv), [spam](results/spam_performance.csv)) as well as a condensed summary of [average performance](results/summary.csv), which appear in the results and appendix.
