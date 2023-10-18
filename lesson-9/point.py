# Создайте файл point.py. Делайте задание в этом файле.
# Вам необходимо создать класс Point (точка на координатной плоскости), у которой будет два поля: x, y.

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

# Добавьте метод distance_to_zero - который будет возвращать расстояние от точки до начала координат (0, 0). Например
# для точки Point(3, 4) это расстояние будет равно 5 (по теореме Пифагора)

    def distance_to_zero(self):
        to_zero = (self.x ** 2 + self.y ** 2) ** 0.5
        return to_zero

# Добавьте метод distance_to_point, который принимает другую точку, и ищет расстояние между ними.

    def distance_to_point(self, other_p):
        dx = self.x - other_p.x
        dy = self.y - other_p.y
        to_point = (dx ** 2 + dy ** 2) ** 0.5
        return to_point


# Скопируйте код из комментария к слайду и проверьте, что он выводит ожидаемый результат.

p1 = Point(3, 4)
p2 = Point(3, 10)
p3 = Point(10, 10)

print('Distance between p1 and zero point:', p1.distance_to_zero())
print('Distance between p2 and zero point:', p2.distance_to_zero())
print('Distance between p3 and zero point:', p3.distance_to_zero())
print('Distance between p1 and p1:', p1.distance_to_point(p1))
print('Distance between p1 and p2:', p1.distance_to_point(p2))
print('Distance between p2 and p1:', p2.distance_to_point(p1))
print('Distance between p1 and p3:', p1.distance_to_point(p3))
print('Distance between p2 and p3:', p2.distance_to_point(p3))