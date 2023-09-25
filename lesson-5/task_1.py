# Напишите функцию is_year_leap, которая принимает число (год) и возвращает True если год високосный, False если нет.

def is_year_leap(year: int):
    if year % 4 == 0:
        return 'True'
    else:
        return 'False'


leap = is_year_leap(2000)
assert leap == 'True'