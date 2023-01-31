from pprint import pprint

from CSVReader import CSVReader

if __name__ == '__main__':
    reader = CSVReader()
    pprint(reader.sort_by("temperature"))
