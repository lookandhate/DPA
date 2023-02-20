import csv
from datetime import datetime
from typing import TypedDict, Callable


class WeatherEntry(TypedDict):
    num: int
    longitude: float
    latitude: float
    temperature: float
    date: datetime


class CSVReader:
    def __init__(self):
        self._file_name = "data.csv"
        self._data: list[WeatherEntry] = []

        self._read_file(self._file_name)

    def _read_file(self, file_path):
        with open(file_path) as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)  # skip header
            for row in reader:
                self._data.append(
                    {
                        "num": int(row[0]),
                        "longitude": float(row[1]),
                        "latitude": float(row[2]),
                        "temperature": float(row[3]),
                        "date": datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S"),
                    }
                )

    def sort_by(self, key: str) -> list[WeatherEntry]:
        return sorted(self._data, key=lambda x: x[key])

    def get_entries_by_criteria(self, key: str, value) -> list[WeatherEntry]:
        return [entry for entry in self._data if entry[key] == value]

    def get_entries_by_functional_criteria(self, func: Callable) -> list[WeatherEntry]:
        return [entry for entry in self._data if func(entry)]

    def new_entry(self, longitude, latitude, tempature):
        self._data.append(WeatherEntry(num=len(self._data),
                                       longitude=longitude,
                                       latitude=latitude,
                                       tempature=tempature,
                                       date=datetime.now()))

    def save(self):
        with open("new.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(self._data)
