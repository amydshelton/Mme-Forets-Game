import pandas as pd
import numpy as np

df = pd.read_csv("Raw data/test3.csv", header=0)


#fill in empty age (n=7) with median age (47)
df.loc[ df['Age Demographic Core'].isnull(), 'Age Demographic Core']='47'


df['Sex_Num'] = df['Sex Demographic Core'].map( {'Female':0, 'Male':1} ).astype(float)

#fill in empty race (n=18) with most common race (white)
df.loc[ df['Race (Census) Race'].isnull(),'Race (Census) Race']='White'


df['Race_Num'] = df['Race (Census) Race'].map ( {'(Multiple)':0, 'American Indian or Alaska Native':1, 'Asian Indian':2, 'Black or African American':3, 'Chinese':4, 'Filipino':5, 'Hispanic (Any race)':6,'Japanese':7, 'Korean':8, 'Native Hawaiian':9, 'Other Asian':10, 'Other Pacific Islander':11,'Samoan':12, 'Some Other Race':13, 'Vietnamese':14, 'White':15} ).astype(float)

df['Region_Num'] = df['Region Demographic'].map ( {'East North Central (IL, IN, MI, OH, WI)':0, 'East South Central (AL, KY, MS, TN)':1, 'Middle Atlantic (NJ, NY, PA)':2, 'Mountain (AZ, CO, ID, MT, NV, NM, UT, WY)':3, 'New England (CT, ME, MA, NH, RI, VT)':4, 'Pacific (AK, CA, HI, OR, WA)':5, 'South Atlantic (DE, FL, GA, MD, NC, SC, VA, WV, DC)':6,'West North Central (IA, KS, MN, MO, NE, ND, SD)':7, 'West South Central (AR, LA, OK, TX)':8} ).astype(float)

#fill in empty grade completed (n=7) with median grade completed (13)
df.loc[ df['Highest Grade Completed Demographic'].isnull(),'Highest Grade Completed Demographic']=13

#fill in empty employment status (n=4) with most common (working fulltime))
df.loc[ df['Employment Status Work Demographic Core'].isnull(),'Employment Status Work Demographic Core']='Working Fulltime'

df['Employment_Status_Num'] = df['Employment Status Work Demographic Core'].map ( {'Keeping House':0, 'Other':1, 'Retired':2, 'School':3, 'Temp Not Working':4,'Unemployed, Laid Off':5, 'Working Fulltime':6, 'Working Parttime':7} ).astype(float)

#fill in empty marital status (n=1) with most common (married))
df.loc[ df['Marital Status Work Demographic Core (Are you currently -- married, widowed, divorced, separated, or have you never been married?)'].isnull(),'Marital Status Work Demographic Core (Are you currently -- married, widowed, divorced, separated, or have you never been married?)']='Married'


df['Marital_Status_Num'] = df['Marital Status Work Demographic Core (Are you currently -- married, widowed, divorced, separated, or have you never been married?)'].map ( {'Divorced':0, 'Married':1, 'Never Married':2, 'Separated':3, 'Widowed':4} ).astype(float)

# delete all the columns with strings
df = df.drop(['Id','Year of Survey Core', 'Sex Demographic Core', 'Race (Census) Race','Region Demographic','Employment Status Work Demographic Core','Marital Status Work Demographic Core (Are you currently -- married, widowed, divorced, separated, or have you never been married?)'],axis=1)

#rename the columns
df.columns=['Age','Highest_Grade','Sex','Race','Region','Employment_Status','Marital_Status']

df.to_csv('output.csv')


#fill in empty family income (n=399) with predicted family income based on demo data up until now

