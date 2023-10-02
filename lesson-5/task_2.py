# Напишите функцию generate_natural_cubes(n), которая принимает число n и возвращает список, состоящий из кубов первых n
# натуральных чисел. То есть [1**3, 2**3, 3**3, ..., n**3]. Обязательно использование генераторов списков.
def generate_natural_cubes(n: int) -> list[int]:
    return [i ** 3 for i in range(1, n+1)]


assert generate_natural_cubes(0) == []
assert generate_natural_cubes(1) == [1]
assert generate_natural_cubes(5) == [1, 8, 27, 64, 125]
assert generate_natural_cubes(10) == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]