data_dict= {

    'religious': {
        'title': 'Religiosity', 
        'question': 'To what extent do you consider yourself a religious \
                     person? Are you...', 
        'answers': {
            'Not Religious':0, 
            'Slightly Religious':1, 
            'Moderately Religious':2, 
            'Very Religious':3
        }
    },

    'spiritual': {
        'title': 'Spirituality',
        'question': 'To what extent do you consider yourself a spiritual \
                     person? Are you...', 
        'answers': {
            'Not Spiritual':0,
            'Slightly Spiritual':1, 
            'Moderately Spirtual':2, 
            'Very Spiritual':3
        }
    },
    
    'party': {
        'title': 'Political Party',
        'question': 'Do you usually think of yourself as a Republican, \
                     Democrat, or Independent?', 
        'answers': {
            'Strong Republican':0,
            'Not Strong Republican':1,
            'Independent, Near Republican':2,
            'Independent':3,
            'Independent, Near Democrat':4,
            'Not Strong Democrat':5,
            'Strong Democrat':6, 
            'Other Party':'NaN'
        }
    },
    
    'death_penalty': {
        'title': 'Death Penalty',
        'question': 'Do you favor or oppose the death penalty for persons \
                     convicted of murder?', 
        'answers': {
            'Oppose':0,
            'Favor':1,
            "Don't Know":'NaN'
        }
    },
    
    'court_harsh': {
        'title': 'Courts & Criminals',
        'question': 'In general, do you think the courts deal too harshly or \
                     not harshly enough with criminals? ', 
        'answers': {
            'Not Harsh Enough':0, 
            'About Right':1, 
            'Too Harsh': 2, 
            "Don't Know":'NaN'
        }
    },
    
    'bar': {
        'title': 'Frequency of Going to a Bar',
        'question': 'How often do you go to a bar or tavern?', 
        'answers': {
            'Never':0,
            'Once a Year':1,
            'Several Times a Year':2,
            'Once a Month':3,
            'Several Times a Month':4,
            'Several Times a Week':5,
            'Almost Daily':6
        }
    },
    
    'tv': {
        'title': 'Hours Watching TV',
        'question': 'On an average day, about how many hours do you personally \
                     spend watching television?', 
        'answers': {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9 to 12': 9,
            '13 or higher': 10
        }
    },
    
    'relatives': {
        'title': 'Socializing with Relatives',
        'question': 'How often do you spend a social evening with relatives?', 
        'answers': {
            'Never':0,
            'Once a Year':1,
            'Several Times a Year':2, 
            'Once a Month':3,
            'Several Times a Month':4, 
            'Several Times a Week':5, 
            'Almost Daily':6
        }
    },
    
    'spanking': {
        'title': 'Spanking Children',
        'question': 'To what extent do you agree or disagree that it is \
                     sometimes necessary to discipline a child with a good, \
                     hard spanking?', 
        'answers': {
            'Strongly Disagree':0,
            'Disagree':1,
            'Agree':2,
            'Strongly Agree':3,
            "Don't Know":'NaN'
        }
    },
    
    'income_distribution': {
        'title': 'Income Redistribution',
        'question': "On a scale from 1 to 7, where 1 indicates that the \
                     government ought to reduce income inequality, and 7 means \
                     that the government should not reduce income inequality, \
                     how would you rate yourself?", 
        'answers': {
            '1 (Government should reduce income differences)':1, 
            '2':2, 
            '3':3, 
            '4':4, 
            '5':5, 
            '6':6, 
            '7 (Government should not reduce income differences)':7
        }
    }, 
    
    'standard_of_living': {
        'title': 'Standard of Living Compared to Parents',
        'question': 'Compared to your parents when they were the age you are \
                     now, how do you think your own standard of living compares?', 
        'answers': {
            'Much Worse':0, 
            'Somewhat Worse':1, 
            'About the Same':2,
            'Somewhat Better':3,
            'Much Better':4
        }
    },
    
    'birth_control': {
        'title': 'Birth Control for Young People',
        'question': 'To what extent do you agree or disagree that methods of \
                     birth control should be available to teenagers between \
                     the ages of 14 and 16 if their parents do not approve?', 
        'answers': {
            'Strongly Disagree':0,
            'Disagree':1,
            'Agree':2,
            'Strongly Agree':3,
            "Don't Know":'NaN'
        }
    },
    
    'immigration': {
        'title': 'Number of Immigrants in the U.S.',
        'question': 'Do you think the number of immigrants to America nowadays \
                     should be...',
        'answers': {
            "Can't Choose":'NaN',
            'Reduced a Lot':0,
            'Reduced a Little':1,
            'Remain the Same as It Is':2,
            'Increased a Little':3,
            'Increased a Lot':4
        }
    },
    
    'affirmative_action': {
        'title': 'Affirmative Action for African-Americans',
        'question': 'To what extent do you agree or disagree with preferential \
                     hiring and promotion for African-Americans?', 
        'answers': {
            "Don't Know":'NaN', 
            'Strongly Oppose Preference for African-Americans':0, 
            'Oppose Preference for African-Americans':1, 
            'Support Preference for African-Americans':2, 
            'Strongly Support Preference for African-Americans':3
        }
    },
    
    'gun': {
        'title': 'Guns in the Home',
        'question': 
        'Do you have any guns or revolvers in your home?', 
        'answers': {
            'No':0,
            'Yes':1
        }
    },

    'tax_approp': {
        'title': 'Appropriateness of Taxation Levels',
        'question': 'Do you consider the amount of federal income tax which \
                     you have to pay as too high, about right, or too low?', 
        'answers': {
            'Too Low':0, 'About Right':1,'Too High':2, "Don't Know":'NaN'
        }
    },
    
    'divorce_ease': {
        'title': 'Ease of Divorce',
        'question': 'Should divorce in this country be easier or more \
                     difficult to obtain than it is now?', 
        'answers': {
            "Don't Know":'NaN',
            'Easier':0,
            'Stay Same':1, 
            'More Difficult':2
        }
    },
    
    'numb_children': {
        'title': 'Ideal Number of Children',
        'question': 'What do you think is the ideal number of children for a \
                     family to have?', 
        'answers': {
            'None':0, 
            'One':1, 
            'Two':2, 
            'Three':3, 
            'Four':4, 
            'Five':5, 
            'Six':6, 
            'Seven or more':7
        }
    }
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
                if data_dict[first_level_key][second_level_key]\
                            [third_level_key] == 'NaN':
                    continue
                else:
                    answer_level_dict[data_dict[first_level_key]\
                                               [second_level_key]\
                                               [third_level_key]] = \
                                               third_level_key
        reversed_data_dict[first_level_key] = answer_level_dict


columns_ordered_by_predictive_power = ['party', 'tv', 'relatives',
                                       'income_distribution', 'religious', 
                                       'spiritual', 'standard_of_living', 
                                       'bar', 'immigration', 'birth_control', 
                                       'spanking', 'affirmative_action', 
                                       'numb_children', 'divorce_ease', 
                                       'court_harsh', 'tax_approp', 
                                       'death_penalty', 'gun'] 

columns_ordered_by_decreasing_N = ['religious', 'spiritual', 'party', 
                                   'death_penalty', 'court_harsh', 'bar', 
                                   'relatives', 'income_distribution', 'tv', 
                                   'spanking', 'standard_of_living', 
                                   'immigration', 'gun', 'tax_approp', 
                                   'affirmative_action', 'divorce_ease', 
                                   'numb_children', 'birth_control']
    # these are in order from lowest number of missing data points to 
    #   highest number

full_columns_ordered_by_decreasing_N = ['age', 'highest_grade'] + \
                                       columns_ordered_by_decreasing_N

full_columns_ordered_by_predictive_power = ['age', 'highest_grade'] + \
                                           columns_ordered_by_predictive_power


