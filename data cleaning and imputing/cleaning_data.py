import pandas as pd
import sys

sys.path.append("/Users/greglaughlin/Desktop/Hackbright/HB_Project")

from universals import data_dict


df = pd.read_csv("../GSS/2010 and 2012 results for variables of interest.csv", header=0)


### FILL IN MISSING BASIC DEMOGRAPHIC DATA WITH MOST COMMON ANSWER/MEDIAN ###

#fill in empty age (n=7) with median age (47)
df.loc[ df['Age Demographic Core'].isnull(), 'Age Demographic Core']='47'

#fill in empty race (n=18) with most common race (white)
df.loc[ df['Race (Census) Race'].isnull(),'Race (Census) Race']='White'

#fill in empty grade completed (n=7) with median grade completed (13)
df.loc[ df['Highest Grade Completed Demographic'].isnull(),'Highest Grade Completed Demographic']=13

#fill in empty employment status (n=4) with most common (working fulltime))
df.loc[ df['Employment Status Work Demographic Core'].isnull(),'Employment Status Work Demographic Core']='Working Fulltime'

#fill in empty marital status (n=1) with most common (married))
df.loc[ df['Marital Status Work Demographic Core (Are you currently -- married, widowed, divorced, separated, or have you never been married?)'].isnull(),'Marital Status Work Demographic Core (Are you currently -- married, widowed, divorced, separated, or have you never been married?)']='Married'



### CONVERT STRINGS TO FLOATS, RENAME VARIABLES, REORDER BY N ####

df['age'] = df["Age Demographic Core"].astype(float)

df['sex'] = df['Sex Demographic Core'].map( data_dict['sex']['answers'] ).astype(float)

df['race'] = df['Race (Census) Race'].map ( data_dict['race']['answers'] ).astype(float)

df['region'] = df['Region Demographic'].map ( data_dict['region']['answers'] ).astype(float)

df['highest_grade'] = df["Highest Grade Completed Demographic"]

df['employment_status'] = df['Employment Status Work Demographic Core'].map ( data_dict['employment_status']['answers'] ).astype(float)

df['marital_status'] = df['Marital Status Work Demographic Core (Are you currently -- married, widowed, divorced, separated, or have you never been married?)'].map ( data_dict['marital_status']['answers'] ).astype(float)

df['religious'] = df['Religious Person Relig (To what extent do you consider yourself a religious person?)'].map( data_dict['religious']['answers']).astype(float)

df['spiritual'] = df['Spiritual Person Relig (To what extent do you consider yourself a spiritual person?)'].map( data_dict['spiritual']['answers']).astype(float)

df['party'] = df['Political Party Politics'].map( data_dict['party']['answers']).astype(float)

df['lib_cons'] = df['Liberalism-Conservatism Politics'].map( data_dict['lib_cons']['answers']).astype(float)

df['death_penalty'] = df['Death Penalty for Murderers Govt'].map( data_dict['death_penalty']['answers']).astype(float)

df['court_harsh'] = df['Court Harshness Govt (In general, do you think the courts in this area deal too harshly or not harshly enough with criminals?)'].map( data_dict['court_harsh']['answers']).astype(float)

df['income'] = df['Inflation-adjusted Family Income Demographic Work Core '].astype(float)

#convert income to buckets

df['sex_partners'] = df['Sex Partners in 5 Years Sex (Now think about the past five year, and including the past 12 months, how many sex partners have you had in that five year period?)'].map( data_dict['sex_partners']['answers']).astype(float)

df['sex_freq'] = df['Sex Frequency in Last Year Sex'].map( data_dict['sex_freq']['answers']).astype(float)

df['bar'] = df['Go to Bar or Tavern Society'].map( data_dict['bar']['answers']).astype(float)

df['tv'] = df['Daily Hours Watching TV Tech']

df['relatives'] = df['Spend a Social Evening with Relatives Society'].map( data_dict['relatives']['answers']).astype(float)

df['spanking'] = df['Spanking Family (Sometimes necessary to discipline a child with a good, hard, spanking?)'].map( data_dict['spanking']['answers']).astype(float)

df['income_distribution'] = df["Income Distribution from Washington Govt (Some people think that the government in Washington ought to reduce the income differences between the rich and the poor, perhaps by raising the taxes of wealthy families or by giving income assistance to the poor. Others think that the government should not concern itself with reducing this income difference between the rich and the poor. What score comes closest to the way you feel? (1 = Government Should Reduce Difference, 7 = Government Shouldn't Take Action))"]

df['standard_living'] = df['Standard of Living Compared to Parents Society (Compared to your parents when they were the age you are now, do you think your own standard of living now is much better, somewhat better, about the same, somewhat worse, or much worse than theirs was?)'].map( data_dict['standard_living']['answers']).astype(float)

df['birth_control'] = df['Birth Control for Young Govt Sex (Methods of birth control should be available to teenagers between the ages of 14 and 16 if their parents do not approve)'].map( data_dict['birth_control']['answers']).astype(float)

df['immigration'] = df['Immigration Govt (Do you think the number of immigrants to America nowadays should be...)'].map( data_dict['immigration']['answers']).astype(float)

df['govt_help_poor'] = df["Govt Help Poor Govt (Some people think that the government in Washington should do everything possible to improve the standard of living of all poor Americans. Other people think itis not the government's responsibility, and that each person should take care of himself. Where would you place yourself? (1 = Government should do everything possible; 3 = Agree with both; 5 = Each person should take care of himself))"]

df['govt_help_sick'] = df['Govt Help Sick Govt (Some people think that it is the responsibility of the government in Washington to see to it that people have help in paying for doctors and hospital bills. Others think that these matters are not the responsibility of the federal government and that people should take care of these things themselves. Where would you place yourself on this scale? (1 = Government should help; 3 = Agree with both; 5 = People should help themselves))']

df['govt_more_less'] = df["Govt Do More or Less Govt (Some people think that the government in Washington is trying to do too many things that should be left to individuals and private business. Others disagree and think that the government should do even more to solve our country's problems. Where would you place yourself on this scale? (1 = Government should do more; 3 = Agree with both; 5 = Government does too much))"]

df['govt_help_blacks'] = df["Govt Help Black Govt Race (Some people think that (blacks/negroes/African-Americans) have been discriminated against for so long that the government has a special obligation to help improve their living standards. Others believe that the government should not be giving special treatment to (blacks/negroes/African-Americans). Where would you place yourself? (1 = Government should help blacks; 3 = Agree with both; 5 = No special treatment))"]

df['affirmative_action'] = df['Affirmative Action Black Govt Race (Some people say that because of past discrimination, blacks should be given preference in hiring and promotion. Others say that such preference in hiring and promotion of blacks is wrong because it discriminates against whites. What about your opinion?)'].map( data_dict['affirmative_action']['answers']).astype(float)

df['gun'] = df['Gun in Home Guns'].map( data_dict['gun']['answers']).astype(float)

df['tax_approp'] = df['Tax Appropriateness Govt (Do you consider the amount of federal income tax which you have to pay as too high, about right, or too low?)'].map( data_dict['tax_approp']['answers']).astype(float)

df['divorce_ease'] = df['Divorce Ease Govt Family (Should divorce in this country be easier or more difficult to obtain than it is now?)'].map( data_dict['divorce']['answers']).astype(float)

df['numb_children'] = df["Ideal Number of Children in Family Family"]


# delete all the old columns 
df = df.drop(['Id','Year of Survey Core', 'Age Demographic Core', 'Sex Demographic Core', 'Race (Census) Race', 'Highest Grade Completed Demographic', 'Region Demographic','Employment Status Work Demographic Core','Marital Status Work Demographic Core (Are you currently -- married, widowed, divorced, separated, or have you never been married?)', 'Religious Person Relig (To what extent do you consider yourself a religious person?)', 'Spiritual Person Relig (To what extent do you consider yourself a spiritual person?)', 'Political Party Politics', 'Liberalism-Conservatism Politics', 'Death Penalty for Murderers Govt', 'Court Harshness Govt (In general, do you think the courts in this area deal too harshly or not harshly enough with criminals?)', 'Sex Partners in 5 Years Sex (Now think about the past five year, and including the past 12 months, how many sex partners have you had in that five year period?)', 'Sex Frequency in Last Year Sex', 'Go to Bar or Tavern Society', 'Spend a Social Evening with Relatives Society', 'Spanking Family (Sometimes necessary to discipline a child with a good, hard, spanking?)', 'Standard of Living Compared to Parents Society (Compared to your parents when they were the age you are now, do you think your own standard of living now is much better, somewhat better, about the same, somewhat worse, or much worse than theirs was?)', 'Birth Control for Young Govt Sex (Methods of birth control should be available to teenagers between the ages of 14 and 16 if their parents do not approve)', 'Immigration Govt (Do you think the number of immigrants to America nowadays should be...)','Affirmative Action Black Govt Race (Some people say that because of past discrimination, blacks should be given preference in hiring and promotion. Others say that such preference in hiring and promotion of blacks is wrong because it discriminates against whites. What about your opinion?)', 'Gun in Home Guns','Tax Appropriateness Govt (Do you consider the amount of federal income tax which you have to pay as too high, about right, or too low?)', 'Divorce Ease Govt Family (Should divorce in this country be easier or more difficult to obtain than it is now?)', 'Ideal Number of Children in Family Family','Inflation-adjusted Family Income Demographic Work Core ', 'Daily Hours Watching TV Tech', "Income Distribution from Washington Govt (Some people think that the government in Washington ought to reduce the income differences between the rich and the poor, perhaps by raising the taxes of wealthy families or by giving income assistance to the poor. Others think that the government should not concern itself with reducing this income difference between the rich and the poor. What score comes closest to the way you feel? (1 = Government Should Reduce Difference, 7 = Government Shouldn't Take Action))", "Govt Help Poor Govt (Some people think that the government in Washington should do everything possible to improve the standard of living of all poor Americans. Other people think itis not the government's responsibility, and that each person should take care of himself. Where would you place yourself? (1 = Government should do everything possible; 3 = Agree with both; 5 = Each person should take care of himself))", "Govt Help Sick Govt (Some people think that it is the responsibility of the government in Washington to see to it that people have help in paying for doctors and hospital bills. Others think that these matters are not the responsibility of the federal government and that people should take care of these things themselves. Where would you place yourself on this scale? (1 = Government should help; 3 = Agree with both; 5 = People should help themselves))", "Govt Do More or Less Govt (Some people think that the government in Washington is trying to do too many things that should be left to individuals and private business. Others disagree and think that the government should do even more to solve our country's problems. Where would you place yourself on this scale? (1 = Government should do more; 3 = Agree with both; 5 = Government does too much))", "Govt Help Black Govt Race (Some people think that (blacks/negroes/African-Americans) have been discriminated against for so long that the government has a special obligation to help improve their living standards. Others believe that the government should not be giving special treatment to (blacks/negroes/African-Americans). Where would you place yourself? (1 = Government should help blacks; 3 = Agree with both; 5 = No special treatment))"],axis=1)

# save out clean data
df.to_csv('cleaned.csv')


