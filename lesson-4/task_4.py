# Программа загадывает случайное число от 0 до 100.
# Пользователь пытается угадать, вводя числа.
# Если пользователь угадал - выведите поздравление и завершите программу.
# Если пользователь не угадал, подскажите ему в какую сторону идти. То есть, если число пользователя слишком большое -
# выведите “не угадал, число больше загаданного”. Если меньше - выведите “не угадал, число меньше загаданного”.

import random
x = random.randrange(0, 100)
y = int(input('Try to guess the number: '))
while x != y:
    if x < y:
        print('Oops! Your number is greater')
        y = int(input('Guess the number again: '))
    elif x > y:
        print('Oops! Your number is less')
        y = int(input('Guess the number again: '))
    else:
        break
print('Congratulations! You won :)')