from sqlalchemy.orm import Session
import models, schemas


def get_weather(db: Session, id: int):
    return db.query(models.Weather).filter(models.Weather.id == id).first()


def get_weathers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Weather).offset(skip).limit(limit).all()


def create_weather(db: Session, weather: schemas.WeatherCreate):
    db_weather = models.Weather(**weather.dict())
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather
