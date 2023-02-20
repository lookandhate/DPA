from pprint import pprint

from CSVReader import CSVReader

if __name__ == '__main__':
    reader = CSVReader()
    pprint(reader.sort_by("date"))
    long, lat, temp = input('Введите новые данные(Долгота, широта, температура: ').split()
    reader.new_entry(long, lat, temp)
    reader.save()