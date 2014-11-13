
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import sessionmaker, scoped_session



ENGINE = create_engine("sqlite:///GSS_project.db", echo=False)
dbsession = scoped_session(sessionmaker(bind = ENGINE, autocommit = False, autoflush = False))


Base = declarative_base()
Base.query = dbsession.query_property()

### Class declarations go here

class PlaySession(Base):
    __tablename__ = 'playsessions'

    session_id =            Column(Integer, primary_key = True)
    age =     		        Column(Float, nullable = False)
    sex =                   Column(Integer, nullable = False)
    american_indian =       Column(Integer, nullable = False)
    asian_indian  =         Column(Integer, nullable = False)
    black  =                Column(Integer, nullable = False)
    chinese  =              Column(Integer, nullable = False)
    filipino  =             Column(Integer, nullable = False)
    hispanic  =             Column(Integer, nullable = False)
    japanese  =             Column(Integer, nullable = False)
    korean  =               Column(Integer, nullable = False)
    multiple  =             Column(Integer, nullable = False)
    hawaiian  =             Column(Integer, nullable = False)
    asian  =                Column(Integer, nullable = False)
    pacific_islander  =     Column(Integer, nullable = False)
    samoan  =               Column(Integer, nullable = False)
    other_race  =           Column(Integer, nullable = False)
    vietnamese  =           Column(Integer, nullable = False)
    white  =                Column(Integer, nullable = False)
    east_north_central  =   Column(Integer, nullable = False)
    east_south_central  =   Column(Integer, nullable = False)
    middle_atlantic =       Column(Integer, nullable = False)
    mountain  =             Column(Integer, nullable = False)
    new_england  =          Column(Integer, nullable = False)
    pacific =               Column(Integer, nullable = False)
    south_atlantic  =       Column(Integer, nullable = False)
    west_north_central =    Column(Integer, nullable = False)
    west_south_central =    Column(Integer, nullable = False)
    keeping_house =         Column(Integer, nullable = False)
    other_employment =      Column(Integer, nullable = False)
    retired =               Column(Integer, nullable = False)
    school =                Column(Integer, nullable = False)
    temp_not_working =      Column(Integer, nullable = False)
    unemployed =            Column(Integer, nullable = False)
    fulltime =              Column(Integer, nullable = False)
    parttime =              Column(Integer, nullable = False)
    divorced =              Column(Integer, nullable = False)
    married =               Column(Integer, nullable = False)
    never_married =         Column(Integer, nullable = False)
    separated =             Column(Integer, nullable = False)
    widowed =               Column(Integer, nullable = False)
    highest_grade =         Column(Float, nullable = False)
    predicted_religious =   Column(Integer, nullable = True)
    religious =             Column(Integer, nullable = True) 
    predicted_spiritual =   Column(Integer, nullable = True)
    spiritual =             Column(Integer, nullable = True) 
    predicted_party =       Column(Integer, nullable = True)
    party =                 Column(Integer, nullable = True) 
    predicted_lib_cons =    Column(Integer, nullable = True)
    lib_cons =              Column(Integer, nullable = True) 
    predicted_death_penalty = Column(Integer, nullable = True)
    death_penalty =         Column(Integer, nullable = True) 
    predicted_court_harsh = Column(Integer, nullable = True)
    court_harsh =           Column(Integer, nullable = True) 
    predicted_bar =         Column(Integer, nullable = True)
    bar =                   Column(Integer, nullable = True) 
    predicted_tv =          Column(Integer, nullable = True)
    tv =                    Column(Integer, nullable = True) 
    predicted_relatives =   Column(Integer, nullable = True)
    relatives =             Column(Integer, nullable = True) 
    predicted_spanking =    Column(Integer, nullable = True)
    spanking =              Column(Integer, nullable = True) 
    predicted_income_distribution = Column(Integer, nullable = True)
    income_distribution =   Column(Integer, nullable = True) 
    predicted_standard_of_living = Column(Integer, nullable = True)
    standard_of_living =    Column(Integer, nullable = True)     
    predicted_birth_control = Column(Integer, nullable = True)
    birth_control =         Column(Integer, nullable = True)
    predicted_immigration = Column(Integer, nullable = True)
    immigration =           Column(Integer, nullable = True)     
    predicted_govt_help_poor = Column(Integer, nullable = True)
    govt_help_poor =        Column(Integer, nullable = True)
    predicted_govt_help_sick = Column(Integer, nullable = True)
    govt_help_sick =        Column(Integer, nullable = True) 
    predicted_govt_more_less = Column(Integer, nullable = True)
    govt_more_less =   Column(Integer, nullable = True)    
    predicted_govt_help_blacks = Column(Integer, nullable = True)
    govt_help_blacks =       Column(Integer, nullable = True) 
    predicted_affirmative_action = Column(Integer, nullable = True)
    affirmative_action =    Column(Integer, nullable = True) 
    predicted_gun =         Column(Integer, nullable = True)
    gun =                   Column(Integer, nullable = True) 
    predicted_tax_approp =  Column(Integer, nullable = True)
    tax_approp =            Column(Integer, nullable = True) 
    predicted_divorce_ease = Column(Integer, nullable = True)
    divorce_ease =   Column(Integer, nullable = True) 
    predicted_numb_children = Column(Integer, nullable = True)
    numb_children =    Column(Integer, nullable = True)     

    def add_play_session(self):
    	dbsession.add(self)
    	dbsession.commit()

    def commit_play_session(self):
        dbsession.commit()

    def ordered_parameter(self):
        all_qs = [self.age, self.sex, self.american_indian, self.asian_indian, self.black, self.chinese, self.filipino, self.hispanic, self.japanese, self.korean, self.multiple, self.hawaiian, self.asian, self.pacific_islander, self.samoan, self.other_race, self.vietnamese, self.white, self.east_north_central, self.east_south_central, self.middle_atlantic, self.mountain, self.new_england, self.pacific, self.south_atlantic, self.west_north_central, self.west_south_central, self.keeping_house, self.other_employment, self.retired, self.school, self.temp_not_working, self.unemployed, self.fulltime, self.parttime, self.divorced, self.married, self.never_married, self.separated, self.widowed, self.highest_grade, self.religious, self.spiritual, self.party, self.lib_cons, self.death_penalty, self.court_harsh, self.bar, self.tv, self.relatives, self.spanking, self.income_distribution, self.standard_of_living, self.birth_control, self.immigration, self.govt_help_poor, self.govt_help_sick, self.govt_more_less, self.govt_help_blacks, self.affirmative_action, self.gun, self.tax_approp, self.divorce_ease, self.numb_children]
        answered_qs = [item for item in all_qs if item != None]
        return answered_qs
        #strip nones off


def main():

	global Base
	Base.metadata.create_all(ENGINE)

if __name__ == "__main__":
	main()