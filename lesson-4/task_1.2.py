# Вывести на экран числа кратные 5 от 0 до 100 включительно.
# Сделать это с помощью функции range c шагом 1 и вложенным if

for n in range(0, 101):
    if n % 5 == 0:
        print(n)