# Дано число. Если оно положительно - выведите positive, если отрицательно - negative, если равно нулю - zero.

n = int(input())
if n > 0:
    print('positive')
elif n < 0:
    print('negative')
else:
    print('zero')