# Программа выводит на экран числа от 0 до 100.
# После вывода каждого числа спрашивайте у пользователя “Should we break?”.
# Если он ответил “yes” - завершите программу.
# Иначе - продолжайте вывод чисел.

for i in range(0, 101):
    print(i)
    n = input('Should we break? ')
    if n == 'yes':
        break