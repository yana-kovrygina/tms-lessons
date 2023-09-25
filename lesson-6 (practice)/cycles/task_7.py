# Дан словарь "слово" -> число. Вывести ключ, соответствующий максимальному значению.
# Пример: {'a': 1, 'b': 2} -> 'b'.

my_dict = {'a': 1, 'b': 2, 'c': 50, 'd': 100, 'e': 5}
m = None
key = None
for k, v in my_dict.items():
    if m is None or v > m:
        m = v
        key = k

print(key)