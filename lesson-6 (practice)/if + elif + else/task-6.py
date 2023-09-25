# Дан номер месяца (число от 1 до 12). Выведите пору года, которой этот месяц принадлежит: зима, весна, лето или осень.

month = int(input())
if month in (3, 4, 5):
    print('spring')
elif month in (6, 7, 8):
    print('summer')
elif month in (9, 10, 11):
    print('autumn')
else:
    print('winter')