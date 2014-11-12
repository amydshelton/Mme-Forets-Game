import pandas as pd

import sys
import numpy as np

sys.path.append("/Users/greglaughlin/Desktop/Hackbright/HB_Project")

from universals import column_order

df = pd.read_csv("imputed.csv", header=0)

# removing first column because it's duplicative - it's just the index column and pandas will assign that again anyway
df = df.ix[:,1:]


# For income, bucket data
df['income_bucket'] = pd.cut(df['income'], bins = [-1, 10000, 20000, 30000, 40000, 50000, 75000, 100000, 200000, 5000000000],labels = False)
labels = np.array('0 1 2 3 4 5 6 7 8'.split()) 
df['income_bucket'] = labels[df['income_bucket']] 
# del df ['income']


### NOT WORKING!!

#put income_bucket in the right spot in the df, where income was
full_column_order = ['age', 'sex', 'race', 'region', 'highest_grade', 'employment_status', 'marital_status', 'income'] + column_order
cols = full_column_order[:] #copy so we don't mutate the original
for x in df.columns:
	if x not in cols:
		cols.append(x)

df[cols]

df.to_csv('bucketed.csv')