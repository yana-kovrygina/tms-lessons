# Пользователь вводит произвольную строку. Выведите кортеж из уникальных символов введённой строки.

line = list(input('Please, type the line: '))
unique = set(line)
unique = tuple(unique)
print('The unique symbols of the line: ', unique)
