
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
    race =                  Column(Integer, nullable = False)
    region =                Column(Integer, nullable = False)
    highest_grade =	        Column(Float, nullable = False)
    employment_status =     Column(Integer, nullable = False)
    marital_status =        Column(Integer, nullable = False)
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
        all_qs = [self.age, self.sex, self.race, self.region, self.highest_grade, self.employment_status, self.marital_status, self.religious, self.spiritual, self.party, self.lib_cons, self.death_penalty, self.court_harsh, self.bar, self.tv, self.relatives, self.spanking, self.income_distribution, self.standard_of_living, self.birth_control, self.immigration, self.govt_help_poor, self.govt_help_sick, self.govt_more_less, self.govt_help_blacks, self.affirmative_action, self.gun, self.tax_approp, self.divorce_ease, self.numb_children]
        answered_qs = [item for item in all_qs if item != None]
        return answered_qs
        #strip nones off


def main():

	global Base
	Base.metadata.create_all(ENGINE)

if __name__ == "__main__":
	main()