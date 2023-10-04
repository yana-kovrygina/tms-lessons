# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.
# Пример:
# Ввод пользователя: a b c d e f
# Результат программы: ['b', 'c', 'd', 'f']
# Используйте функцию filter.
# Список всех гласных английского языка: a, e, i, o, u

def remove_vowels(symbols_list):
    symbols_list_new = list(filter(lambda i: i not in ['a', 'e', 'i', 'o', 'u'], symbols_list))
    return symbols_list_new


print(remove_vowels(list(input('Please, enter only latin symbols and spaces only: ').split())))