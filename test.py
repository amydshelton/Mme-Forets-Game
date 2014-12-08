from model import dbsession, RandomForest
from sklearn.ensemble import RandomForestClassifier
import pandas as pd 

from universals import columns_ordered_by_predictive_power, full_columns_ordered_by_predictive_power

test_data = [31, 16]

rf_object = dbsession.query(RandomForest).filter_by(output_var = 'party').first()

print rf_object

forest = rf_object.rf_model
forest = eval(forest)

print forest

prediction = forest.predict(test_data)[0]

print prediction