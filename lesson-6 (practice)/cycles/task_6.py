# Дан словарь "слово" -> число. Вывести максимальное число среди значений словаря.
# Пример: {'a': 1, 'b': 2} -> 2. Смотрите примечание в слайде.

my_dict = {'a': 1, 'b': 2, 'c': -1, 'd': 100}
m = None

for value in my_dict.values():
    if m is None or value > m:
        m = value

print(m)