from pprint import pprint

from CSVReader import CSVReader

if __name__ == '__main__':
    reader = CSVReader()
    print(f'Сортировка по критерию:')

    sort_criteria = input('Выберете критерий для сортировки: \n1)По температуре\n2)По номеру измерения\n3)По дате: ')
    try:
        sort_criteria = int(sort_criteria)
    except ValueError:
        print("Ошибка при приведении выбора к числу. Повторите еще раз")
        exit()

    match sort_criteria:
        case 1:
            pprint(reader.sort('temperature'))

        case 2:
            pprint(reader.sort('num'))

        case 3:
            pprint(reader.sort('date'))

    print('=' * 20)

    print("Итерация")
    for i in reader:
        print(i)

    print('=' * 20)

    print('Генератор')
    for i in reader.generator():
        print(i)
