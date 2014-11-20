data_dict= {
	'race': 
		{'question': 'What is your race?', 'answers': 
			{'Multiple':'multiple', 'American Indian or Alaska Native':'american_indian', 'Asian Indian':'asian_indian', 'Black or African American':'black', 'Chinese':'chinese', 'Filipino':'filipino', 'Hispanic (Any race)':'hispanic','Japanese':'japanese', 'Korean':'korean', 'Native Hawaiian':'hawaiian', 'Other Asian':'asian', 'Other Pacific Islander':'pacific_islander','Samoan':'samoan', 'Some Other Race':'other_race', 'Vietnamese':'vietnamese', 'White':'white'}},
	'sex': 
		{'question': 'Sex', 'answers': 
			{'Female':0, 'Male':1}},
	'region': 
		{'question': 'Region of Current Residence', 'answers': 
			{'East North Central (IL, IN, MI, OH, WI)':'east_north_central', 'East South Central (AL, KY, MS, TN)':'east_south_central', 'Middle Atlantic (NJ, NY, PA)':'middle_atlantic', 'Mountain (AZ, CO, ID, MT, NV, NM, UT, WY)':'mountain', 'New England (CT, ME, MA, NH, RI, VT)':'new_england', 'Pacific (AK, CA, HI, OR, WA)':'pacific', 'South Atlantic (DE, FL, GA, MD, NC, SC, VA, WV, DC)':'south_atlantic','West North Central (IA, KS, MN, MO, NE, ND, SD)':'west_north_central', 'West South Central (AR, LA, OK, TX)':'west_south_central'}},
	'employment_status': 
		{'question': 'Last week were you working full time, part time, going to school, keeping house, or what?', 'answers': 
			{'Keeping House':'keeping_house', 'Other':'other_employment', 'Retired':'retired', 'School':'school', 'Temp Not Working':'temp_not_working','Unemployed, Laid Off':'unemployed', 'Working Fulltime':'fulltime', 'Working Parttime':'parttime'}},
	'marital_status': 
		{'question': 'Are you currently married, widowed, divorced, separated, or have you never been married?', 'answers': 
			{'Divorced':'divorced', 'Married':'married', 'Never Married':'never_married', 'Separated':'separated', 'Widowed':'widowed'}},
	'religious': 
		{'title': 'Religiosity', 'question': 'To what extent do you consider yourself a religious person? Are you...', 'answers': 
			{'Not Religious':0, 'Slightly Religious':1, 'Moderately Religious':2, 'Very Religious':3}},
	'spiritual': 
		{'title': 'Spirituality','question': 'To what extent do you consider yourself a spiritual person? Are you...', 'answers': 
			{ 'Not Spiritual':0,'Slight Spiritual':1, 'Moderate Spirtual':2, 'Very Spiritual':3}},
	'party': 
		{'title': 'Political Party','question': 'Generally speaking, do you usually think of yourself as a Republican, Democrat, or Independent?', 'answers': 
			{ 'Strong Republican':0, 'Not Strong Republican':1, 'Independent, Near Republican':2, 'Independent':3, 'Independent, Near Democrat':4, 'Not Strong Democrat':5, 'Strong Democrat':6, 'Other Party':'NaN'}},
	'lib_cons': 
		{'title': 'Conserativism to Liberalism','question': 'Where would you place yourself on a scale from extremely conservative to extremely liberal?', 'answers': 
			{ 'Extremely Conservative':0,'Conservative':1, 'Slightly Conservative':2, 'Moderate':3, 'Slightly Liberal':4, 'Liberal':5, 'Extremely Liberal':6, "Don't Know":'NaN'}},
	'death_penalty': 
		{'title': 'Death Penalty','question': 'Do you favor or oppose the death penalty for persons convicted of murder?', 'answers': 
			{'Oppose':0,'Favor':1,"Don't Know":'NaN'}},
	'court_harsh': 
		{'title': 'Courts & Criminals','question': 'In general, do you think the courts deal too harshly or not harshly enough with criminals? ', 'answers': 
			{'Not Harsh Enough':0, 'About Right':1, 'Too Harsh': 2, "Don't Know":'NaN'}},
	'bar': 
		{'title': 'Frequency of Going to a Bar','question': 'How often do you go to a bar or tavern?', 'answers':
			{'Never':0, 'Once a Year':1, 'Several Times a Year':2, 'Once a Month':3,'Several Times a Month':4, 'Several Times a Week':5, 'Almost Daily':6}},
	'tv': 
		{'title': 'Hours Watching TV','question': 'On an average day, about how many hours do you personally spend watching television?', 'answers':
			{'0': 0,'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9 to 12': 9, '13 or higher': 10}},
	'relatives': 
		{'title': 'Socializing with Relatives','question': 'How often do you spend a social evening with relatives?', 'answers': 
			{'Never':0, 'Once a Year':1, 'Several Times a Year':2, 'Once a Month':3,'Several Times a Month':4, 'Several Times a Week':5, 'Almost Daily':6}},
	'spanking':
		{'title': 'Spanking Children','question': 'Do you strongly agree, agree, disagree, or strongly disagree that it is sometimes necessary to discipline a child with a good, hard spanking?', 'answers': 
			{'Strongly Disagree':0,'Disagree':1,'Agree':2,'Strongly Agree':3,"Don't Know":'NaN'}},
	'income_distribution': 
		{'title': 'Income Redistribution','question': "On a scale from 1 to 7, where 1 indicates that the government ought to reduce the income differences between rich and poor, and 7 means that the government should not concern itself with reducing income differences, what score comes closest to the way you feel?", 'answers': 
			{'1 (Government should reduce income differences)':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7 (Government should not reduce income differences)':7}}, 
	'standard_of_living': 
		{'title': 'Standard of Living Compared to Parents','question': 'Compared to your parents when they were the age you are now, do you think your own standard of living now is much better, somewhat better, about the same, somewhat worse, or much worse than theirs was?', 'answers': 
			{'Much Worse':0, 'Somewhat Worse':1, 'About the Same':2,'Somewhat Better':3,'Much Better':4}},
	'birth_control':
		{'title': 'Birth Control for Young People','question': 'Do you strongly agree, agree, disagree, or strongly disagree that methods of birth control should be available to teenagers between the ages of 14 and 16 if their parents do not approve?', 'answers': 
			{'Strongly Disagree':0,'Disagree':1,'Agree':2,'Strongly Agree':3,"Don't Know":'NaN'}},
	'immigration': 
		{'title': 'Number of Immigrants in the U.S.','question': 'Do you think the number of immigrants to America nowadays should be...', 'answers': 
			{"Can't Choose":'NaN','Reduced a Lot':0,'Reduced a Little':1,'Remain the Same as It Is':2,'Increased a Little':3,'Increased a Lot':4}},
	'govt_help_poor': 
		{'title': "Government's Obligation to the Poor",'question': "Some people think that the government in Washington should do everything possible to improve the standard of living of all poor Americans; they would rate themselves a 1 on this scale. Other people think it is not the government's responsibility, and that each person should take care of himself; they would rate themselves a 5. How would you rate yourself?", 'answers': 
			{'1 (Government should do all it can)':1, '2':2, '3 (Agree with both)':3, '4':4, '5 (Each person should take care of him/herself)':5}},
	'govt_help_sick': 
		{'title': "Government's Obligation to the Sick",'question': 'In general, some people think that it is the responsibility of the government in Washington to see to it that people have help in paying for doctors and hospital bills. Others think that these matters are not the responsibility of the federal government and that people should take care of these things themselves. Where would you place yourself on this scale?', 'answers': 
			{'1 (Government should help)':1, '2':2, '3 (Agree with both)':3, '4':4, '5 (Each person should take care of his/her own medical bills)':5}},
	'govt_more_less': 
		{'title': "Government's Obligation to the Poor",'question': "Some people think that the government in Washington is trying to do too many things that should be left to individuals and private businesses. Others disagree and think that the government should do even more to solve our country's problems. Where would you place yourself on this scale?", 'answers': 
			{'1 (Government should do more)':1, '2':2, '3 (Agree with both)':3, '4': 4, '5 (Government doing too much)':5}},
	'govt_help_blacks': 
		{'title': "Government's Obligation to African-Americans",'question': 'Some people think that African-Americans have been discriminated against for so long that the government has a special obligation to help improve their living standards. Others believe that the government should not be giving special treatment to African-Americans. Where would you place yourself on this scale?', 'answers': 
			{'1 (Government should help)':1, '2':2, '3 (Agree with both)':3, '4':4, '5 (African-Americans should receive no special treatment)':5}},
	'affirmative_action': 
		{'title': 'Affirmative Action for African-Americans','question': 'Some people say that because of past discrimination, blacks should be given preference in hiring and promotion. Others say that such preference in hiring and promotion of blacks is wrong because it discriminates against whites. Are you for or against preferential hiring and promotion of blacks?', 'answers': 
			{"Don't Know":'NaN', 'Strongly Oppose Preference for Blacks':0, 'Oppose Preference for Blacks':1, 'Support Preference for Blacks':2, 'Strongly Support Preference for Blacks':3}},
	'gun': 
		{'title': 'Guns in the Home','question': 'Do you have any guns or revolvers in your home?', 'answers': 
			{'No':0,'Yes':1}},
	'tax_approp': 
		{'title': 'Appropriateness of Taxation Levels','question': 'Do you consider the amount of federal income tax which you have to pay as too high, about right, or too low?', 'answers': 
			{'Too Low':0, 'About Right':1,'Too High':2, "Don't Know":'NaN'}},
	'divorce_ease': 
		{'title': 'Ease of Divorce','question': 'Should divorce in this country be easier or more difficult to obtain than it is now?', 'answers': 
			{"Don't Know":'NaN','Easier':0, 'Stay Same':1, 'More Difficult':2}},
	'numb_children': 
		{'title': 'Ideal Number of Children','question': 'What do you think is the ideal number of children for a family to have?', 'answers': 
			{'None':0, 'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven or more':7}}
	}


# Reverse data dict so we can translate numbers back into words

reversed_data_dict={}

for first_level_key in data_dict:
	answer_level_dict = {}
	for second_level_key in data_dict[first_level_key]: 
		if second_level_key != 'answers':
			continue
		else:
			for third_level_key in data_dict[first_level_key][second_level_key]:
				if data_dict[first_level_key][second_level_key][third_level_key] == 'NaN':
					continue
				else:
					answer_level_dict[data_dict[first_level_key][second_level_key][third_level_key]] = third_level_key
		reversed_data_dict[first_level_key] = answer_level_dict


columns_ordered_by_predictive_power = ['party','income_distribution', 'tv', 'relatives', 'religious', 'spiritual', 'standard_of_living', 'immigration', 'birth_control', 'bar','spanking','affirmative_action', 'divorce_ease', 'numb_children','court_harsh', 'tax_approp','death_penalty', 'gun'] 

columns_ordered_by_decreasing_N = ['religious', 'spiritual', 'party', 'death_penalty', 'court_harsh','bar', 'tv', 'relatives', 'spanking', 'income_distribution', 'standard_of_living', 'birth_control', 'immigration', 'affirmative_action', 'gun', 'tax_approp', 'divorce_ease', 'numb_children'] 


full_columns_ordered_by_decreasing_N = ['age', 'highest_grade'] + columns_ordered_by_decreasing_N

full_columns_ordered_by_predictive_power = ['age', 'highest_grade'] + columns_ordered_by_predictive_power

	# these are in order from lowest number of missing data points to highest number
