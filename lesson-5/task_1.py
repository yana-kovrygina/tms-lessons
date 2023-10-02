# Напишите функцию is_year_leap, которая принимает число (год) и возвращает True если год високосный, False если нет.

def is_year_leap(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


assert is_year_leap(2024)
assert is_year_leap(2000)
assert not is_year_leap(1900)
assert not is_year_leap(2023)
