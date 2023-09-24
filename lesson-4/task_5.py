n = int(input('Please, enter any number: '))
summ = 0
while n != 0:
    summ += n % 10
    n //= 10
print('The sum is: ', summ)
