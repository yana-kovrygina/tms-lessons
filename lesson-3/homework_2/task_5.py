m = str(input('Please, enter the month: '))
m = m.lower()
dict_a = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}
print('Number of days: ', dict_a[m])