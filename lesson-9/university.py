# Создайте файл university.py. Делайте задание в этом файле.
# Импортируйте класс Student из первого задания

from student import Student

# Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.

students = [Student('Richard Roe', 4),
            Student('Jack House', 5),
            Student('Helen Roe', 7),
            Student('Mary Major', 9),
            Student('John Doe', 10)]


# Посчитайте суммарную стипендию для всех студентов.
# Посчитайте количество отличников (используйте метод is_excellent).
# Заверните код для пунктов 4 и 5 к функции calc_sum_scholarship и get_excellent_student_count

def calc_sum_scholarship(self):
    return sum([student.get_scholarship() for student in students])


def get_excellent_student_count(self):
    count = 0
    for student in students:
        if student.is_excellent():
            count += 1
    return count


# вызов обеих функций и вывод результатов на экран

sum_scholarship = calc_sum_scholarship(students)
print(f'Total scholarship is: {sum_scholarship}')

excellent_students = get_excellent_student_count(students)
print(f'Number of excellent students: {excellent_students}')
