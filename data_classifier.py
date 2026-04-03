"""
Central classifier. For choice of dataset, method and redundancy (for thermal case), 
can evaluate accuracy of classifier (on Training and Unseen data)
"""
from Tsetlin_machine_framework import Memory, train_machine, classify
from analysis_data_handling import prep_data, log_results
from tqdm import tqdm


def test_classifier(dataset, method, N):
    """
    use thermodynamic/classical Tsetlin machine for classification and obtain
    testing/training accuracy
    ----------
    dataset :[str] name of dataset 
    (choose from: 'mushroom', 'breast_cancer', 'spam', 'tictactoe', 'income')
    method : [str] type of classifier (choose from: 'Classical','Therm')
    N : [int] redundancy, number of gate duplicates for therm. classifier
    -------
    accuracy_test, accuracy_train: [num] classification accuracy
    """
    
    X_train, X_test, Y_train, Y_test, Y_train_flip, dim_memory = prep_data(dataset)
    conditions = []
    not_conditions = []
    num_rules = 10
    training_loops = 100
    for i in tqdm(range(num_rules)):
        rule = Memory(0.9,0.1, dim_memory)
        train_machine(rule, X_train, Y_train, training_loops, method, N)
        conditions.extend([rule.get_condition()])
        
        not_rule = Memory(0.9,0.1, dim_memory)
        train_machine(not_rule, X_train, Y_train_flip, training_loops, method, N)
        not_conditions.extend([not_rule.get_condition()])
        
    correct_test = 0
    for i in range(len(X_test)):
        output = classify(X_test[i],conditions,not_conditions, method, N)
        if output == Y_test[i]:
            correct_test+=1
    accuracy_test = correct_test*100/len(X_test)
    
    correct_train = 0
    for i in range(len(X_train)):
        output = classify(X_train[i],conditions,not_conditions, method, N)
        if output == Y_train[i]:
            correct_train+=1
    accuracy_train = correct_train*100/len(X_train)
        
    results_dict ={'Dataset': dataset,
                    'Method': (method, 'N=',N),
                    'Avg Training Accuracy': accuracy_train, 
                    'Avg. Testing Accuracy': accuracy_test, 
                    'Training/Test': '80/20', 
                    'Rules': num_rules,
                    'Training loops': training_loops} 
    # log_results(csv_path, results_dict)
    print("Train Accuracy: ", accuracy_train)
    print("Test Accuracy: ", accuracy_test)
    return accuracy_test, accuracy_train
 

"""
dataset: 'mushroom', 'breast_cancer', 'spam', 'tictactoe', 'income'
method: 'Classical', 'Therm'
N: (corresponds to redundancy for thermodynamic classifier)
"""

test_classifier('spam', 'Classical', 0)

