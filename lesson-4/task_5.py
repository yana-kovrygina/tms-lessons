# Пользователь вводит произвольное число. Посчитайте сумму цифр этого числа используя операторы % и //
# Пример для числа 12.
# Ответ должен быть получен примерно так:
# answer = 12 % 10 # 2
# answer += 12 // 10  # 1
# print(answer)  # 3

n = int(input('Please, enter any number: '))
summ = 0
while n != 0:
    summ += n % 10
    n //= 10
print('The sum is: ', summ)
