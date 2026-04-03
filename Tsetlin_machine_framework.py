"""
Contains class and functions for classification. 
"""
from random import random
from random import choice
import matplotlib.pyplot as plt
import numpy as np
from network import evaluate_condition_therm # with signal qubit

def evaluate_condition(observation, condition, method, N):
    """
    determines whether observation satisfies condition
    ----------
    observation : [vector] object - described by True/False features
    condition : [vector] rule - which features must be True/False
    method : [string] 'Therm' or 'Classical'
    N : [integer] redundancy for Thermodynamic classifier
    -------
    output : Boolean (whether object satisfies rule)
    """
    if method == 'Classical':
        output = evaluate_condition_class(observation, condition)
    elif method == 'Therm':
        output = evaluate_condition_therm(observation, condition, N)
        
    return output
        

def evaluate_condition_class(observation, condition):
    """
    ----------
    observation : [vector] object - described by True/False features
    condition : [vector] rule - which features must be True/False
    -------
    truth_value_of_condition : does the observation satify the condition?
    """
    truth_value_of_condition = True
    for i in range(len(observation)):
        #literal required to be True but is False
        if condition[0,2*i] == 1 and observation[i] == 0: 
            truth_value_of_condition = False
            break
        # literal required to be False but is True
        elif condition[0,(2*i)+1] == 1 and observation[i] == 1: 
            truth_value_of_condition = False
            break
    return truth_value_of_condition
        


class Memory:
    """
    stores memory states to produce rule for classification
    contains functions for tuning memory states and extracting rule
    """
    def __init__(self, forget_value, memorize_value, dim_memory):
        self.dim_memory = dim_memory 
        self.memory = np.zeros(dim_memory)# 1d array ie: vector
        for i in range(len(self.memory)):
            self.memory[i] = 5
        self.forget_value = forget_value # float
        self.memorize_value = memorize_value #float
    
    def get_memory(self):
        return self.memory
    
    def get_condition(self):
        # literal remembered = 1, forgotten = 0
        condition = np.zeros((1,len(self.memory)))
        for literal in range(len(self.memory)):
            if self.memory[literal] >= 6:
                condition[0][literal] = 1
        return condition
        
    def memorize(self, literal):
        # with some randomization, increment value of literal(integer) in memory
        if random() <= self.memorize_value and self.memory[literal] < 10:
            self.memory[literal] += 1
            
    def forget(self, literal):
        # with randomization, decrement value of literal(integer) in memory
        if random() <= self.forget_value and self.memory[literal] > 1:
            self.memory[literal] -= 1
            
    def memorize_always(self, literal):
        # w/out randomization, increment value of literal in memory
        if  self.memory[literal] < 10:
            self.memory[literal] += 1
            
    def plot_memory(self, labels):
        position = self.memory
        plt.bar(range(0,len(self.memory)), position, color= '#C79FEF')
        plt.xticks(range(len(position)),labels, rotation= 'vertical')
        plt.ylim(0,10)
        plt.axhline(y=5, color='r', linestyle='--')
        plt.show()    
 
    
def type_i_feedback(observation, memory, method, N): 
    """ 
    Type I Feedback (frequent patterns) 
    1) Check if condition part of the rule is True, if so memorize all the True literals. 
    2) Forget all remaining (False) literals. 
    """ 
    condition = memory.get_condition()
    if evaluate_condition(observation, condition, method, N) == True: 
        for i in range(len(observation)): 
            if observation[i] == 1: # literal is true 
                memory.memorize(2*i) # memorize literal 
                memory.forget(2*i+1) # forget NOT literal 
            elif observation[i] == 0: #literal is false 
                memory.memorize(2*i+1) #memorize NOT literal 
                memory.forget(2*i) #forget literal
    
    elif evaluate_condition(observation, condition, method, N) == False:
        for i in range(len(condition[0])):
            memory.forget(i)
            
def type_ii_feedback(observation, memory, method, N): 
    """ 
    Type II Feedback (For class False, ie: planes)   
    If object evaluates to True, memorize all False literals. 
    no randomization - increment always performed. 
    """ 
    if evaluate_condition(observation, memory.get_condition(), method, N) == True: 
        for i in range(len(observation)): 
            if observation[i] == 0: #literal is false
                memory.memorize_always(2*i) # memorize literal 
            elif observation[i] == 1: #literal is true 
                memory.memorize_always(2*i+1) #memorize NOT literal
 
            
# In practice, we use both Type I and II feedback. 
# - Type I allows us to recognise patterns.
# - Type II increasing discriminating power of the machine.

def train_machine(rule, data, target, training_loops, method, N):
    """
    rule: [vector] literals which have memory position > 5
    data: [dataset] training dataset
    training_loops: [integer] number of times rule is tested and tuned
    method: [string] 'Classical' or 'Therm'
    N: [integer] redundancy for thermodynamic classifier
    """
    for i in range(0,training_loops):
        rand = choice(range(len(target)))
        observation = data[rand]
        if target[rand] == 1:
            type_i_feedback(observation, rule, method, N)
        elif target[rand] == 0:
            type_ii_feedback(observation, rule, method, N)
            
        
def classify(observation, conditions, not_conditions, method, N):
    """
    each rule casts a vote for a particular class
    ----------
    observation : [vector] object being classifier
    conditions : [vector] rule for target class
    not_conditions : [vector] rule for 'not' target class
    method : [string] 'Classical' or 'Therm'
    N : [integer] redundancy for 'Therm'
    -------
    whether input object is classified into target class
    """
    vote_sum = 0
    for condition in conditions:
        if evaluate_condition(observation, condition, method, N) == True:
            vote_sum += 1
    for not_condition in not_conditions:
        if evaluate_condition(observation, not_condition, method, N) == True:
            vote_sum -= 1
    if vote_sum >= 0:
        return True
    else:
        return False



