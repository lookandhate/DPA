from sqlalchemy import Column, Integer, Double, Date

from database import  Base

class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Double)
    latitude = Column(Double)
    temperature = Column(Double)
    date = Column(Date)
