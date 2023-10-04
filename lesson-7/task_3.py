# Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре. Вам по-прежнему нужно
# удалить все гласные. При этом вывести результат нужно вывести сохранив изначальный регистр.
# Пример:
# Ввод пользователя: a B c d E F
# Результат программы: ['B', 'c', 'd', 'F']
# Используйте функцию filter.

def remove_vowels(symbols_list):
    symbols_list_new = list(filter(lambda i: i not in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'], symbols_list))
    return symbols_list_new


print(remove_vowels(list(input('Please, enter only latin symbols and spaces only: ').split())))