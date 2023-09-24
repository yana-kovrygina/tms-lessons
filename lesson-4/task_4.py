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