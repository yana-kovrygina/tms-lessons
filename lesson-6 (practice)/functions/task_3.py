# Напишите функцию simple_compare, которая принимает два числа и возвращает True, если первое число меньше второго.
# Иначе возвращает False.

def simple_compare(a, b):
    return a < b


assert simple_compare(-1, 5) == True
assert simple_compare(0, 0) == False
assert simple_compare(7, 1) == False