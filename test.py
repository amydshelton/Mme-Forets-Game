from model import dbsession, RandomForest
from sklearn.ensemble import RandomForestClassifier
import pandas as pd 

from universals import columns_ordered_by_predictive_power, full_columns_ordered_by_predictive_power

# test_data = [31, 16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

test_data = [31,16,6]
rf_object = dbsession.query(RandomForest).filter_by(output_var = 'tv').first()

print rf_object.output_var

forest = rf_object.rf_model

print forest

prediction = forest.predict(test_data)[0]

print prediction