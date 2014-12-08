from model import dbsession, RandomForest
from sklearn.ensemble import RandomForestClassifier
import pandas as pd 

from universals import columns_ordered_by_predictive_power, \
                       full_columns_ordered_by_predictive_power

def store_model():
    global columns_ordered_by_predictive_power, dbsession,\
           full_columns_ordered_by_predictive_power

    forest = RandomForestClassifier(n_estimators = 100)

    df = pd.read_csv('data cleaning and imputing/imputed.csv', header=0, 
                     index_col=0)

    for item in columns_ordered_by_predictive_power:
        random_forest = RandomForest()

        var_name = item
        
        random_forest.output_var = var_name

        # determine what column number the current variable is in, to be used in 
        # setting up the training data
        column_of_var_in_full_list = full_columns_ordered_by_predictive_power.\
                                    index(var_name) + 1  
                                    # +1 because python slicing is not inclusive

        ### Set up training data ###
        train_data = df.ix[:,0:column_of_var_in_full_list] # trimming it down to just the columns 
                                              # up to and including the target 
                                              # variable

        train_data_values = train_data.values #converting out of dataframe
        features_of_training_data = train_data_values[0::,0:-1:] # whole dataset 
                                                                 # minus last 
                                                                 # column, which is 
                                                                 # target variable
        target_variable = train_data_values[0::,-1] # slices off the last column, 
                                                    # which is the target variable 

        # Fit the training data to the target and create the decision trees
        model = forest.fit(features_of_training_data, target_variable)
        setattr(random_forest, 'rf_model', model)
        # random_forest.rf_model = model

        column_of_var_in_short_list = columns_ordered_by_predictive_power.index\
                                      (var_name)

        for variable in columns_ordered_by_predictive_power\
            [:column_of_var_in_short_list]:
            model_var_name = str(variable) + "_input"
            setattr(random_forest, model_var_name, 1)
            # print getattr(random_forest, model_var_name)

        for variable in columns_ordered_by_predictive_power\
            [column_of_var_in_short_list:]:
            model_var_name = str(variable) + "_input"
            setattr(random_forest, model_var_name, 0)
            # print getattr(random_forest, model_var_name)


        dbsession.add(random_forest)
        
        dbsession.commit()


store_model()