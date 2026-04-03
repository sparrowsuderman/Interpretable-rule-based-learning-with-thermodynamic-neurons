from thermal_gates import AND, OR, NOT


def evaluate_condition_therm(observation, condition, N):
    """
    observation: [vector] describes item being considered
    condition: [vector]  features that are remembered
    -------
    truth_value_of_condition : does the observation satify the condition?
    """
    result = 1
    for i in range(len(observation)):
        output = single_feature_network(observation[i], condition[0,2*i],condition[0,2*i+1], N)
        result = AND(result, output, N)
    return result
    

def single_feature_network(x,c1,c2, N):
    """
    determines whether a feature satisfies its corresponding literal 
    (corresponds to single-feature network)
    ----------
    x : [0,1] truth value for feature
    c1 : [0,1] True literal
    c2 : [0,1] False literal
    N : [integer] gate redundancy (number of duplicates)
    -------
    outputC : [0,1] returns 1 if c1=1 and x=1 or c2=1 and x=0, otherwise 0.
    """
    NOTx = NOT(x, N)
    NOTc1 = NOT(c1, N)
    NOTc2 = NOT(c2, N)
    
    outputA1 = AND(NOTx, NOTc1, N)
    outputA2 = AND(x, c1, N)
    
    outputB1 = OR(outputA1, outputA2, N)
    outputB2 = AND(x, NOTc2, N)
    
    outputC = OR(outputB1, outputB2, N)

    return outputC

        
    
   

