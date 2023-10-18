# Создайте файл person.py, делайте задание в этом файле.
# Создайте класс Person. У класса должно быть три поля: full_name, age, gender, которые должны заполняться в
# конструкторе. Будем считать что поле gender имеет тип str и может быть либо 'M' (male), либо 'F' (female).

from datetime import datetime


class Person:
    def __init__(self, full_name: str, age: int, gender: str):
        self.full_name = full_name
        self.age = age
        self.gender = gender

# Добавьте в класс метод print_person_info, который печатает на экран строку:
# "Person: {full_name} ({gender}), {age} years old"

    def print_person_info(self):
        return f'Person: {self.full_name} ({self.gender}), {self.age} years old'

# Добавьте метод get_birth_year, которая возвращает год рождения человека (рассчитанное как 2023 - age)
# Замените цифру 2023 на текущий год (чтобы ваша программа работала правильно даже через год). Текущий год можно взять с
# помощью модуля datetime

    def get_birth_year(self):
        return f'Birth year: {datetime.now().year - self.age}'

# # создание объекта
# p = Person('John Doe', 35, 'M')
#
# # вызов метода класса и вывод результата на экран
# print(p.print_person_info())
# print(p.get_birth_year())