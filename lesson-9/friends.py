# Создайте файл friends.py. Делайте задание в этом файле.
# Импортируйте класс Person из первого задания

from person import Person

my_friends = [Person('Richard Roe', 27, 'M'),
              Person('Jack House', 35, 'M'),
              Person('Helen Roe', 18, 'F'),
              Person('Mary Major', 45, 'F')]

# Выведите информацию о каждом друге на экран.

for friend in my_friends:
    print(friend.print_person_info())


# Найдите среди друзей самого старшего, выведите информацию о нём на экран.
# Выведите на экран информацию о всех друзьях мужского пола (можно использовать функцию filter, либо генератор списков).
# Заверните код из пунктов 5 и 6 в функции get_oldest_person и filter_male_person соответственно.

def get_oldest_person(friends):
    oldest_friend = max(my_friends, key=lambda friend: friend.age)
    return oldest_friend


def filter_male_person(friends):
    male_friends = [friend for friend in my_friends if friend.gender == 'M']
    return male_friends


# вызов обеих функций и вывод результатов на экран

oldest = get_oldest_person(my_friends)
print(f'The oldest person: {oldest.full_name} ({oldest.gender}), {oldest.age}')

male_friends = filter_male_person(my_friends)
print('Male friends: ')
for friend in male_friends:
    print(f'{friend.full_name} ({friend.gender}), {friend.age}')