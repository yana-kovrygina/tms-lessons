# Напишите функцию generate_squares, которая принимает произвольное количество аргументов и возвращает список, состоящий
# из их квадратов.

def generate_squares(*args) -> list:
    return [value ** 2 for value in args]


assert generate_squares(0) == [0]
assert generate_squares(1, 2, 3, 5, 8, 13) == [1, 4, 9, 25, 64, 169]
assert generate_squares(-1, -2, -3, -5, -8, -13) == [1, 4, 9, 25, 64, 169]