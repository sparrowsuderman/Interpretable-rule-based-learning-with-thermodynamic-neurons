"""
Below are logical gates which produce the same outputs as the thermodynamic 
gates. This is done by selecting outputs based on probabilities (which correspond
to the likelihood of excitation of the signal qubit).
This utilises the idea of redundancy in quantum error correction in order to 
improve the accuracy of network. This is done by duplicating each gate and 
outputting 1 if any of the duplicates is one.
"""
import numpy as np
import random

# N is the number of gate duplicates
t = 1 # thermalisation time index, choose from 0 = 25, 1 = 50, 2 = 100, 3 = 150
"""
each row of the probability array corresponds to a thermalisation time 
(number of iterations in simulation):
25; 50; 100; 150
each column corresponds to the P(output = 1 | input)
NOT: P(1|0), P(1|1)
AND/OR: P(1|00), P(1|01), P(1|10), P(1|11)
"""
NOT_prob = np.array([[0.9789831, 0.003909242],
                [0.977626065, 1.26204E-09],
                [0.975251421, 7.42828E-24],
                [0.977626065, 3.87748E-38]])
AND_prob = np.array([[0.002967746, 0.010597384, 0.010597384, 0.976467152],
                     [4.30736E-10, 6.27785E-08, 6.27785E-08, 0.974312484],
                     [4.39756E-25, 2.20672E-19, 2.20672E-19, 0.970497928],
                     [3.95665E-40, 7.04339E-31, 7.04339E-31, 0.970497928]])

OR_prob = np.array([[0.002967746, 0.977145975, 0.977145975, 0.978217848],
                    [4.30736E-10, 0.97523051, 0.97523051, 0.976640353],
                    [4.39756E-25, 0.971851321, 0.971851321, 0.97387029],
                    [4.39756E-25, 0.971851321, 0.971851321, 0.97387029]])


def NOT(input1, N):
    """
    returns output of thermodynamic NOT gate
    ----------
    input1: [0,1] logic value of input
    N: [int] redundancy of gate
    """
    for i in range(N):
        output = NOT_dup(input1)
        if output == 1:
            break
        else:
            output = 0
    return output


def NOT_dup(input1):
    """
    uses probabilities to determine output of thermodynamic NOT gate
    ----------
    input1 : [0,1] logical input value
    -------
    output : computation output
    """
    output = 0
    decider = random.random()

    if input1 == 0:
         if decider<NOT_prob[t][0]:
              output = 1
              
    elif input1 == 1: 
         if decider<NOT_prob[t][1]: 
             output = 1

    return output

def AND(input1,input2, N):
    """
    returns output of thermodynamic AND gate
    ----------
    input1, input2: [0,1] logic value of input
    N: [int] redundancy of gate
    """
    for i in range(N):
        output = AND_dup(input1,input2)
        if output == 1:
            break
        else:
            output = 0
    return output
    


def AND_dup(input1, input2):
    """
    uses probabilities to determine output of thermodynamic AND gate
    ----------
    input1, input2 : [0,1] logical input value
    -------
    output : computation output
    """
    output = 0
    decider = random.random()

    if input1 == 0 and input2 == 0:
        if decider<AND_prob[t][0]:
            output = 1
    
    elif input1 == 0 and input2 == 1:
        if decider<AND_prob[t][1]:
            output = 1

    elif input1 == 1 and input2 == 0:
        if decider<AND_prob[t][2]:
            output = 1

    elif input1 == 1 and input2 == 1:
        if decider<AND_prob[t][3]:
            output = 1
    return output


def OR(input1,input2, N):
    """
    returns output of thermodynamic OR gate
    ----------
    input1, input2: [0,1] logic value of input
    N: [int] redundancy of gate
    """
    for i in range(N):
        output = OR_dup(input1, input2)
        if output == 1:
            break
        else: 
            output = 0
    return output



def OR_dup(input1, input2):
    """
    uses probabilities to determine output of thermodynamic OR gate
    ----------
    input1, input2 : [0,1] logical input value
    -------
    output : computation output
    """
    output = 0
    decider = random.random()

    if input1 == 0 and input2 == 0:
          if decider<OR_prob[t][0]:
              output = 1

    elif input1 == 0 and input2 == 1:
          if decider<OR_prob[t][1]:
              output = 1
              
    elif input1 == 1 and input2 == 0:
          if decider<OR_prob[t][2]:
              output = 1
  
    elif input1 == 1 and input2 == 1:
         if decider<OR_prob[t][3]:
             output = 1
  
    return output






