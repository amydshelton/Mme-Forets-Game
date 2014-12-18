
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Float, String, PickleType
from sqlalchemy.orm import sessionmaker, scoped_session
import os
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from universals import data_dict, reversed_data_dict, \
#                        columns_ordered_by_predictive_power,\
#                        full_columns_ordered_by_predictive_power


DATABASE_URL = os.environ.get("DATABASE_URL","postgresql://localhost:5432/mme_forets_game")
ENGINE = create_engine(DATABASE_URL, echo = False)
# ENGINE = create_engine("sqlite:///Mme_Forets_Game.db", echo=False)
dbsession = scoped_session(sessionmaker(bind = ENGINE, autocommit = False, 
            autoflush = True))


Base = declarative_base()
Base.query = dbsession.query_property()

### Class declarations go here

class PlaySession(Base):
    __tablename__ = 'playsessions'

    session_id =                    Column(Integer, primary_key = True)
    age =                           Column(Float, nullable = False)
    highest_grade =                 Column(Float, nullable = False)
    predicted_party =               Column(Integer, nullable = True)
    party =                         Column(Integer, nullable = True)
    predicted_income_distribution = Column(Integer, nullable = True)
    income_distribution =           Column(Integer, nullable = True)     
    predicted_tv =                  Column(Integer, nullable = True)
    tv =                            Column(Integer, nullable = True)
    predicted_relatives =           Column(Integer, nullable = True)
    relatives =                     Column(Integer, nullable = True) 
    predicted_religious =           Column(Integer, nullable = True)
    religious =                     Column(Integer, nullable = True) 
    predicted_spiritual =           Column(Integer, nullable = True)
    spiritual =                     Column(Integer, nullable = True) 
    predicted_standard_of_living =  Column(Integer, nullable = True)
    standard_of_living =            Column(Integer, nullable = True)  
    predicted_immigration =         Column(Integer, nullable = True)
    immigration =                   Column(Integer, nullable = True)   
    predicted_birth_control =       Column(Integer, nullable = True)
    birth_control =                 Column(Integer, nullable = True)
    predicted_bar =                 Column(Integer, nullable = True)
    bar =                           Column(Integer, nullable = True)
    predicted_spanking =            Column(Integer, nullable = True)
    spanking =                      Column(Integer, nullable = True)
    predicted_affirmative_action =  Column(Integer, nullable = True)
    affirmative_action =            Column(Integer, nullable = True) 
    predicted_divorce_ease =        Column(Integer, nullable = True)
    divorce_ease =                  Column(Integer, nullable = True) 
    predicted_numb_children =       Column(Integer, nullable = True)
    numb_children =                 Column(Integer, nullable = True)     
    predicted_court_harsh =         Column(Integer, nullable = True)
    court_harsh =                   Column(Integer, nullable = True) 
    predicted_tax_approp =          Column(Integer, nullable = True)
    tax_approp =                    Column(Integer, nullable = True) 
    predicted_death_penalty =       Column(Integer, nullable = True)
    death_penalty =                 Column(Integer, nullable = True) 
    predicted_gun =                 Column(Integer, nullable = True)
    gun =                           Column(Integer, nullable = True) 
    total_forets_points =           Column(Integer, nullable = True)
    total_players_points =          Column(Integer, nullable = True) 
    name =                          Column(String(50), nullable = True)
 


    def add_play_session(self):
        dbsession.add(self)
        dbsession.commit()

    def commit_play_session(self):
        dbsession.commit()

    def ordered_parameter(self):
        """ Returns all the data the player has submitted about themselves so 
        far, to serve as the test data for the model """
        all_qs = [self.age, self.highest_grade, self.party, 
                  self.income_distribution, self.tv, self.relatives, 
                  self.religious, self.spiritual, self.standard_of_living, 
                  self.immigration, self.birth_control, self.bar,  
                  self.spanking, self.affirmative_action, self.divorce_ease, 
                  self.numb_children, self.court_harsh, self.tax_approp, 
                  self.death_penalty, self.gun]
        answered_qs = [item for item in all_qs if item != None]
        return answered_qs
        # strip nones off



class RandomForest(Base):
    __tablename__ = 'random_forest'
    rf_id =                         Column(Integer, primary_key = True)
    output_var =                    Column(String(50), nullable = False)    
    party_input =                   Column(Integer, nullable = False)
    income_distribution_input =     Column(Integer, nullable = False)     
    tv_input =                      Column(Integer, nullable = False)
    relatives_input =               Column(Integer, nullable = False) 
    religious_input =               Column(Integer, nullable = False) 
    spiritual_input =               Column(Integer, nullable = False) 
    standard_of_living_input =      Column(Integer, nullable = False)  
    immigration_input =             Column(Integer, nullable = False)   
    birth_control_input =           Column(Integer, nullable = False)
    bar_input =                     Column(Integer, nullable = False)
    spanking_input =                Column(Integer, nullable = False)
    affirmative_action_input =      Column(Integer, nullable = False) 
    divorce_ease_input =            Column(Integer, nullable = False) 
    numb_children_input =           Column(Integer, nullable = False)     
    court_harsh_input =             Column(Integer, nullable = False) 
    tax_approp_input =              Column(Integer, nullable = False) 
    death_penalty_input =           Column(Integer, nullable = False) 
    gun_input =                     Column(Integer, nullable = False)
    rf_model =                      Column(PickleType, nullable = False)


def main():
    global Base
    Base.metadata.create_all(ENGINE)


if __name__ == "__main__":
    main()