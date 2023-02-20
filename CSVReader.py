import csv
from datetime import datetime
from typing import TypedDict, Callable, Self


class WeatherEntry(TypedDict):
    num: int
    longitude: float
    latitude: float
    temperature: float
    date: datetime

    def to_str(self):
        return f'{self.num}: ({self.longitude, self.latitude}, {self.temperature} °C, on {self.date.strptime()}'


class CSVReader:
    def __init__(self):
        self._file_name = "data.csv"
        self._data: list[WeatherEntry] = []

        self._read_file(self._file_name)
        self._current_row = 0

    @classmethod
    def build_from_dict(cls, data: list[WeatherEntry]) -> Self:
        instance = cls()
        instance._data = data
        return instance

    def __iter__(self):
        return self

    def __getitem__(self, item):
        return self._data[self._current_row].get(item)

    def __next__(self):
        if self._current_row >= len(self._data):
            self._current_row = 0
            raise StopIteration
        self._current_row += 1
        return self._data[self._current_row - 1]

    def generator(self):
        while self._current_row < len(self._data):
            yield self._data[self._current_row]
            self._current_row += 1

    def __repr__(self):
        return f'Row: {self._current_row}: {self._data[self._current_row]}'

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

    def sort(self, key: str) -> list[WeatherEntry]:
        return sorted(self._data, key=lambda x: x[key])

    def get_entries_by_criteria(self, key: str, value) -> list[WeatherEntry]:
        return [entry for entry in self._data if entry[key] == value]

    def get_entries_by_functional_criteria(self, func: Callable) -> list[WeatherEntry]:
        return [entry for entry in self._data if func(entry)]
