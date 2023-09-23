m = str(input('Please, type the month: '))
m = m.lower()
d = int(input('Please, type the day: '))
list_m = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november','december']
if m in list_m and d in range(1, 32):
    print('True')
print('False')

# тут же можно не заморачиваться с тем, что в некоторых месяцах нет определенных чисел? :)
# вот второй вариант решения, если вводить номер месяца:

m = int(input('Please, type the month (from 1 to 12): '))
d = int(input('Please, type the day: '))
if m in range(1, 13) and d in range(1, 32):
    print('True')
print('False')