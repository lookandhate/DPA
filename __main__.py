import random


def timestamp(epoch_time: float):
    def is_year_leap(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    total_seconds = int(epoch_time)
    micro_seconds = int((epoch_time - total_seconds) * 1000000)
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    year = 1970
    month = 1
    day = 1
    while True:
        days_in_year = 365
        if is_year_leap(year):
            days_in_year = 366
        if days >= days_in_year:
            year += 1
            days -= days_in_year
        else:
            break
    while True:
        days_in_month = 31
        if month in [4, 6, 9, 11]:
            days_in_month = 30
        elif month == 2:
            days_in_month = 29 if is_year_leap(year) else 28
        if days >= days_in_month:
            month += 1
            days -= days_in_month
        else:
            break
    day += days
    return year, month, day, hours, minutes, seconds, micro_seconds


def get_min_list(data: list | None = None):
    if not data: data = [random.randint(-10 ** 5, 10 ** 5) for _ in range(random.randint(1, 10 * 2))]
    return min(data)
