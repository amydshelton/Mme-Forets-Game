import pandas as pd
import sys

sys.path.append("/Users/greglaughlin/Desktop/Hackbright/HB_Project")

from universals import data_dict, full_columns_ordered_by_decreasing_N


df = pd.read_csv("../GSS/2008, 2010, and 2012 results for variables of interest.csv", header=0)

# removing first column because it's duplicative - it's just the index column and pandas will assign that again anyway. Also removing second column b/c it's year of survey and we don't need that.
df = df.ix[:,2:]


### FILL IN MISSING BASIC DEMOGRAPHIC DATA WITH MEDIAN ###

#fill in empty age (n=16) with median age (47)
df.loc[ df['Age Demographic Core'].isnull(), 'Age Demographic Core']='47'


#fill in empty grade completed (n=12) with median grade completed (13)
df.loc[ df['Highest Grade Completed Demographic'].isnull(),'Highest Grade Completed Demographic']=13


### CONVERT STRINGS TO FLOATS, RENAME VARIABLES####
old_and_new_var_names = [
		('age','Age Demographic Core', 'float'), 
		('highest_grade', "Highest Grade Completed Demographic", 'float'), 
		('tv', 'Daily Hours Watching TV Tech', 'string'), 
		('income_distribution', "Income Distribution from Washington Govt (Some people think that the government in Washington ought to reduce the income differences between the rich and the poor, perhaps by raising the taxes of wealthy families or by giving income assistance to the poor. Others think that the government should not concern itself with reducing this income difference between the rich and the poor. What score comes closest to the way you feel? (1 = Government Should Reduce Difference, 7 = Government Shouldn't Take Action))", 'float'), 
		('numb_children', "Ideal Number of Children in Family Family", 'float'),
		('religious', 'Religious Person Relig (To what extent do you consider yourself a religious person?)', 'string'),
		('spiritual', 'Spiritual Person Relig (To what extent do you consider yourself a spiritual person?)', 'string'), 
		('party', 'Political Party Politics', 'string'), ('death_penalty', 'Death Penalty for Murderers Govt', 'string'), 
		('court_harsh', 'Court Harshness Govt (In general, do you think the courts in this area deal too harshly or not harshly enough with criminals?)', 'string'), 
		('bar', 'Go to Bar or Tavern Society', 'string'), 
		('relatives', 'Spend a Social Evening with Relatives Society', 'string'), 
		('spanking', 'Spanking Family (Sometimes necessary to discipline a child with a good, hard, spanking?)', 'string'), 
		('standard_of_living', 'Standard of Living Compared to Parents Society (Compared to your parents when they were the age you are now, do you think your own standard of living now is much better, somewhat better, about the same, somewhat worse, or much worse than theirs was?)', 'string'), 
		('birth_control', 'Birth Control for Young Govt Sex (Methods of birth control should be available to teenagers between the ages of 14 and 16 if their parents do not approve)', 'string'), 
		('immigration', 'Immigration Govt (Do you think the number of immigrants to America nowadays should be...)', 'string'), 
		('affirmative_action', 'Affirmative Action African-American Govt Race (Some people say that because of past discrimination, African-Americans should be given preference in hiring and promotion. Others say that such preference in hiring and promotion of African-Americans is wrong because it discriminates against whites. What about your opinion?)', 'string'), 
		('gun', 'Gun in Home Guns', 'string'), 
		('tax_approp', 'Tax Appropriateness Govt (Do you consider the amount of federal income tax which you have to pay as too high, about right, or too low?)', 'string'), ('divorce_ease', 'Divorce Ease Govt Family (Should divorce in this country be easier or more difficult to obtain than it is now?)', 'string')]

for name_pair in old_and_new_var_names:
	new_name = name_pair[0]
	old_name = name_pair[1]
	var_type = name_pair[2]
	if var_type == 'float':
		df[new_name] = df[old_name]
	else:
		df[new_name] = df[old_name].map(data_dict[new_name]['answers']).astype(float)
	df = df.drop(old_name, axis = 1)


#Reorder to be in order of decreasing N
# column_order = ['age','highest_grade','religious', 'spiritual', 'party', 'death_penalty', 'court_harsh','bar', 'tv', 'relatives', 'spanking', 'income_distribution', 'standard_of_living', 'birth_control', 'immigration', 'affirmative_action', 'gun', 'tax_approp', 'divorce_ease', 'numb_children'] 

new_df = df[full_columns_ordered_by_decreasing_N]

# save out clean data
new_df.to_csv('cleaned.csv')


