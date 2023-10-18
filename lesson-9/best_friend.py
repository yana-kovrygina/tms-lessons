# Создайте файл best_friend.py. Делайте задание в этом файле.
# Импортируйте класс Person из первого задания

from person import Person

# Создайте переменную my_best_friend класса Person (пускай имена будут вымышленными).
# my_best_friend = Person('Ivan Ivanov', 20, 'M')

my_best_friend = Person('Jane Doe', 40, 'F')

# Выведите информацию my_best_friend на экран (метод print_person_info).
print(my_best_friend.print_person_info())

# Выведите год рождения my_best_friend на экран.
print(my_best_friend.get_birth_year())