# Дан список чисел. Найти максимальное среди них.

# 1.
list_a = [5, 10, 146, -15, 24, 17, -150]
print(max(list_a))

# 2.
list_a = [5, 10, 146, -15, 24, 17, -150]
m = list_a[0]
for i in list_a:
    if i > m:
        m = i
print(m)