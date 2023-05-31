from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/weather/', response_model=schemas.Weather)
async def create_weather(weather: schemas.WeatherCreate, db: Session = Depends(get_db)):
    return crud.create_weather(db, weather=weather)


@app.get("/weather/", response_model=list[schemas.Weather])
async def read_weathers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    weathers = crud.get_weathers(db, skip=skip, limit=limit)
    return weathers


@app.get("/weather/{weather_id}", response_model=schemas.Weather)
async def read_weather(weather_id: int, db: Session = Depends(get_db)):
    db_weather = crud.get_weather(db, weather_id)
    if not db_weather:
        raise HTTPException(status_code=404, detail="Weather not found")

    return db_weather
