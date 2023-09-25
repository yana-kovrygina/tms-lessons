# Дано три числа. Вывести количество положительных чисел среди них.
# 1.
a = int(input())
b = int(input())
c = int(input())
x = 0
if a > 0:
    x += 1
if b > 0:
    x += 1
if c > 0:
    x += 1

print('x')

# 2.
a = int(input())
b = int(input())
c = int(input())
x = 0
for i in [a, b, c]:
    if i > 0:
        x += 1
print(x)