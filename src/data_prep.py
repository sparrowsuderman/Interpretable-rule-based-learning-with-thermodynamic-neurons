# prep data

import numpy as np
import pandas as pd
# !pip install ucimlrepo
from ucimlrepo import fetch_ucirepo 
from sklearn.model_selection import train_test_split
from binarizer import Binarizer

def fetch_data(dataset):
    """
    fetches dataset from repository
    ----------
    dataset : [str] name of dataset
    -------
    X: [array] data
    Y: [vector] class labels
    """
    max_bits_per_feature = 0
    if dataset == 'spam':
        database = fetch_ucirepo(id=94)
        max_bits_per_feature = 4
    if dataset == 'breast_cancer': 
        database =fetch_ucirepo(id=17)
        max_bits_per_feature = 2
    if dataset == 'mushroom':
        database = fetch_ucirepo(id=73) 
    if dataset == 'income':
        database = fetch_ucirepo(id=2)
        max_bits_per_feature = 4
    if dataset == 'tictactoe':
        database = fetch_ucirepo(id=101)
        
    X = database.data.features
    y = database.data.targets.to_numpy().ravel()
    
    return X, y, max_bits_per_feature

def prep_data(dataset, X, y, max_bits_per_feature):
    """
    sorts data into training/testing groups with corresponding class labels
    ----------
    dataset :[str] name of dataset 
    (choose from: 'mushroom', 'breast_cancer', 'spam', 'tictactoe', 'income')
    X: [array] data
    y: [vector] class labels
    ------
    ValueError: when there are more than two possible classes
    -------
    X_train, X_test: [array] training/testing data with ratio 0.8:0.2
    Y_train, Y_test : [vector] class labels for each datapoint in data
    Y_train_flip : [vector] inverse of Y_train for training of rule for opposite class
    dim_memory : [int] number of literals
    """

    
    if dataset == 'income':
        y = np.array([str(val).strip().replace('.', '') for val in y])
        
    unique_vals = np.unique(y)
    print("Unique labels:", np.unique(y))
    if len(unique_vals) != 2:
        raise ValueError("Only binary classification is supported")
    # Map first label → 0, second → 1
    mapping = {val: i for i, val in enumerate(unique_vals)}
    target = np.array([mapping[val] for val in y])
    
    # --- Split columns ---
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns
    numerical_cols = X.select_dtypes(exclude=['object', 'category']).columns

    # Categorical
    if len(categorical_cols) > 0:
        X_cat = pd.get_dummies(X[categorical_cols])
        X_cat = X_cat.to_numpy()
    else:
        X_cat = np.empty((len(X), 0))

    # Numerical
    if len(numerical_cols) > 0:
        b = Binarizer(max_bits_per_feature=max_bits_per_feature)
        b.fit(X[numerical_cols].to_numpy())
        X_num = b.transform(X[numerical_cols].to_numpy())
    else:
        X_num = np.empty((len(X), 0))

    # --- Combine ---
    data = np.hstack([X_num, X_cat])

    X_train, X_test, Y_train, Y_test = train_test_split(data, target, 
                                                        test_size=0.2, shuffle=True)
    Y_train_flip = 1 - Y_train # this is for training the not_rule
    dim_memory = data.shape[1]*2
    print('Data is ready for learning.')
    return X_train, X_test, Y_train, Y_test, Y_train_flip, dim_memory

