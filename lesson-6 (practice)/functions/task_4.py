# Напишите функцию compare, которая принимает два числа и возвращает -1 если первое число меньше второго,
# 1 если первое больше второго, и 0 если они равны. Примеры:
# # compare(100, 200) -> -1
# # compare(200, 100) -> 1
# # compare(10, 10) -> 0

def compare(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0


assert compare(-5, 2) == -1
assert compare(5, -10) == 1
assert compare(0, 0) == 0