data_dict= {
	'race': {'(Multiple)':0, 'American Indian or Alaska Native':1, 'Asian Indian':2, 'Black or African American':3, 'Chinese':4, 'Filipino':5, 'Hispanic (Any race)':6,'Japanese':7, 'Korean':8, 'Native Hawaiian':9, 'Other Asian':10, 'Other Pacific Islander':11,'Samoan':12, 'Some Other Race':13, 'Vietnamese':14, 'White':15},
	'sex': {'Female':0, 'Male':1},
	'region': {'East North Central (IL, IN, MI, OH, WI)':0, 'East South Central (AL, KY, MS, TN)':1, 'Middle Atlantic (NJ, NY, PA)':2, 'Mountain (AZ, CO, ID, MT, NV, NM, UT, WY)':3, 'New England (CT, ME, MA, NH, RI, VT)':4, 'Pacific (AK, CA, HI, OR, WA)':5, 'South Atlantic (DE, FL, GA, MD, NC, SC, VA, WV, DC)':6,'West North Central (IA, KS, MN, MO, NE, ND, SD)':7, 'West South Central (AR, LA, OK, TX)':8},
	'employment_status': {'Keeping House':0, 'Other':1, 'Retired':2, 'School':3, 'Temp Not Working':4,'Unemployed, Laid Off':5, 'Working Fulltime':6, 'Working Parttime':7},
	'marital_status': {'Divorced':0, 'Married':1, 'Never Married':2, 'Separated':3, 'Widowed':4},
	'lib_cons': { 'Extremely Conservative':0,'Conservative':1, 'Slightly Conservative':2, 'Moderate':3, 'Slightly Liberal':4, 'Liberal':5, 'Extremely Liberal':6, "Don't Know":'NaN'},
	'court_harsh': {'Not Harsh Enough':0, 'About Right':1, 'Too Harsh': 2, "Don't Know":'NaN'},
	'party': { 'Strong Republican':0, 'Not Strong Republican':1, 'Independent, Near Republican':2, 'Independent':4, 'Independent, Near Democrat':4, 'Not Strong Democrat':5, 'Strong Democrat':6, 'Other Party':'NaN'},
	'religious': { 'Not Religious':0, 'Slightly Religious':1, 'Moderately Religious':2, 'Very Religious':3},
	'death_penalty': {'Oppose':0,'Favor':1,"Don't Know":'NaN'},
	'spiritual': { 'Not Spiritual':0,'Slight Spiritual':1, 'Moderate Spirtual':2, 'Very Spiritual':3},
	'sex_partners': {'No Partners':0, '1 Partner':1, '2 Partners':2, '3 Partners':3, '4 Partners':4, '5-10 Partners':5, '11-20 Partners':6, '21-100 Partners':7, 'More than 100 Partners':8},
	'sex_freq': {'Not at All':0, 'Once or Twice':1, 'Once a Month':2, '2-3 Times a Month':2, 'Weekly':3, '2-3 Per Week':4, '4+ Per Week':5},
	'bar': {'Never':0, 'Once a Year':1, 'Several Times a Year':2, 'Once a Month':3,'Several Times a Month':4, 'Several Times a Week':5, 'Almost Daily':6},
	'spanking':{'Strongly Disagree':0,'Disagree':1,'Agree':2,'Strongly Agree':3,"Don't Know":'NaN'},
	'bc_young':{'Strongly Disagree':0,'Disagree':1,'Agree':2,'Strongly Agree':3,"Don't Know":'NaN'},
	'relatives': {'Never':0, 'Once a Year':1, 'Several Times a Year':2, 'Once a Month':3,'Several Times a Month':4, 'Several Times a Week':5, 'Almost Daily':6},
	'immigration': {"Can't Choose":'NaN','Reduced a Lot':0,'Reduced a Little':1,'Remain the Same as It Is':2,'Increased a Little':3,'Increased a Lot':4},
	'divorce': {"Don't Know":'NaN','Easier':0, 'Stay Same':1, 'More Difficult':2},
	'affirmative_action': {"Don't Know":'NaN', 'Strongly Oppose Preference for Blacks':0, 'Oppose Preference for Blacks':1, 'Support Preference for Blacks':2, 'Strongly Support Preference for Blacks':3},
	'standard_living': {'Much Worse':0, 'Somewhat Worse':1, 'About the Same':2,'Somewhat Better':3,'Much Better':4},
	'tax_approp': {'Too Low':0, 'About Right':1,'Too High':2, "Don't Know":'NaN'},
	'gun': {'No':0,'Yes':1},
	}


# Reverse data dict so we can translate numbers back into words

reversed_data_dict={}

for key in data_dict:
	second_level_dict = {}
	for second_level_key in data_dict[key]: 
		if data_dict[key][second_level_key] == 'NaN':
			continue
		else:
			second_level_dict[data_dict[key][second_level_key]] = second_level_key
	reversed_data_dict[key] = second_level_dict
