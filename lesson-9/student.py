# Создайте файл student.py. Делайте задание в этом файле.
# Создайте класс Student, с полями full_name, average_mark (средняя оценка).

class Student:
    def __init__(self, full_name: str, average_mark: int):
        self.full_name = full_name
        self.average_mark = average_mark

# Добавьте в класс метод get_scholarship, который подсчитывает и возвращает стипендию данного студента по следующему
# алгоритму:
# Если средняя оценка < 6 - вернуть 60 (рублей)
# Если средняя оценка >= 6, но < 8 - вернуть 80 (рублей)
# Если средняя оценка >= 8 - вернуть 100 (рублей)

    def get_scholarship(self):
        scholarship = 0
        if self.average_mark < 6:
            scholarship += 60
        elif 6 <= self.average_mark < 8:
            scholarship += 80
        else:
            scholarship += 100
        return scholarship

    def is_excellent(self):
        return self.average_mark >= 9


# # вызов обеих функций и вывод результатов на экран
#
# student = Student('Jane Doe', 10)
# print(student.get_scholarship())
# print(student.is_excellent())