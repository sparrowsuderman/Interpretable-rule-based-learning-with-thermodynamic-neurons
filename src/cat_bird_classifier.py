"""
Tsetlin Classifier for a basic dataset - to be used as an example of the principle.
Aim is to classify cats vs birds.
"""
from Tsetlin_machine_framework import Memory, train_machine, classify
import numpy as np

def prep_data(data, not_data, training_split):
    """
    prepare data for training/testing
    ----------
    data : [array] list of objects in target class
    not_data : [array] list of objects not in target class
    training_split : [float] fraction of dataset used for training
    -------
    X_train : [array] training data
    X_test : [array] testing data
    Y_train : [1D array] list of class types for training data
    Y_test : [1D array] list of class types for testing data
    Y_train_flip : [1D array] list of class for training for opposite class
    dim_memory : [integer] number of literal states
    """
    frac = training_split
    x = np.vstack([data,not_data])
    y = np.hstack([np.ones(len(data)),np.zeros(len(not_data))])
    dim_memory = 2*(x.shape[1])


    idx = np.random.permutation(len(x))
    X, Y = x[idx], y[idx]

    split = int(len(X)*frac)
    X_train, X_test = X[:split], X[split:]
    Y_train, Y_test = Y[:split], Y[split:]
    Y_train_flip = 1-Y_train
    
    return X_train, X_test, Y_train, Y_test, Y_train_flip, dim_memory


# Training/Test Data

labels = ['Four legs', 'NOT Four legs',
          'Can fly', 'Can NOT fly',
          'Fur', 'NOT fur',
          'Lays eggs', 'NOT lays eggs',
          'orange', 'NOT orange',
          'brown', 'NOT brown']


cat = np.zeros((6,6))
cat[0] = [1,0,1,0,1,0]
cat[1] = [1,0,1,0,1,1]
cat[2] = [1,0,1,0,0,1]
cat[3] = [1,0,1,0,1,0]
cat[4] = [1,0,1,0,0,0]
cat[5] = [1,0,1,0,0,1]


bird = np.zeros((6,6))
bird[0] = [0,1,0,1,0,0]
bird[1] = [0,1,0,1,0,1]
bird[2] = [0,1,0,1,1,0]
bird[3] = [0,1,0,1,1,1]
bird[4] = [0,1,0,1,1,0]
bird[5] = [0,1,0,1,0,0]

X_train, X_test, Y_train, Y_test, Y_train_flip, dim_memory = prep_data(cat, bird, 0.8)

def print_rule(rule, labels, class_):
    literals = []
    for i in range(len(labels)):
        if rule[0][i]==1:
            literals.append(labels[i])
    print("IF " + " AND ".join(literals) + " THEN ", class_)



def test_classifier(method, N):
    training_loops = 100
    cat_rule = Memory(0.9, 0.1,dim_memory)
    bird_rule = Memory(0.9, 0.1,dim_memory)

    train_machine(cat_rule, X_train, Y_train, training_loops, method, N)
    train_machine(bird_rule, X_train, Y_train_flip, training_loops, method, N)


    cat_condition = cat_rule.get_condition()
    print_rule(cat_condition, labels, 'cat')
    cat_rule.plot_memory(labels)
    bird_condition = bird_rule.get_condition()
    print_rule(bird_condition, labels, 'bird')

    correct_train = 0
    correct_test = 0
    
    for i in range(len(Y_test)):
        output1 = classify(X_test[i], [cat_condition], [bird_condition], method, N)
        output2 = classify(X_test[i], [bird_condition], [cat_condition], method, N)
        if output1 == True and Y_test[i] == 1:
            correct_test += 1
        elif output2 == True and Y_test[i] == 0:
            correct_test +=1
            
    for i in range(len(Y_train)):
        output1 = classify(X_train[i], [cat_condition], [bird_condition], method, N)
        output2 = classify(X_train[i], [bird_condition], [cat_condition], method, N)
        if output1 == True and Y_train[i] == 1:
            correct_train += 1
        elif output2 == True and Y_train[i] == 0:
            correct_train +=1
    

    accuracy_test = correct_test/len(Y_test)*100
    accuracy_train = correct_train/len(Y_train)*100
    print("Test Accuracy: ", accuracy_test, "%")
    print("Train Accuracy: ", accuracy_train, "%")
    return accuracy_test

# Find accuracy of classifier for cat/bird dataset.

method = 'Therm' # 'Classical' or 'Therm'
N = 2 # integer > 0 for 'Therm' (0 for 'Classical')

test_classifier(method, N)


