from datetime import date

from pydantic import BaseModel


class WeatherBase(BaseModel):
    longitude: float
    latitude: float
    temperature: float
    date: date


class WeatherCreate(WeatherBase):
    pass


class Weather(WeatherBase):
    id: int

    class Config:
        orm_mode = True
