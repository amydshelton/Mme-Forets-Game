
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

    session_id =	Column(Integer, primary_key = True)
    age =     		Column(Float, nullable = False)
    sex =  		Column(Integer, nullable = False)
    race =       	Column(Integer, nullable = False)
    region =   		Column(Integer, nullable = False)
    highest_grade =	Column(Float, nullable = False)
    predicted_employment_status = Column(Integer, nullable = True)

    employment_status = Column(Integer, nullable = True)



def main():

	global Base
	Base.metadata.create_all(ENGINE)

if __name__ == "__main__":
	main()