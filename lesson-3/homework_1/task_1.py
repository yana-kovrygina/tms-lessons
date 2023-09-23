sec = int(input('Please, enter the number of seconds: '))
d = sec // (60 * 60 * 24)
h = sec // (60 * 60) % 24
m = sec // 60 % 60
s = sec % 60
print(str(d) + ':' + str(h) + ':' + str(m) + ':' + str(s))

