# Дана строка. Посчитайте сколько раз в ней встречается символ "a".

s = str('aasdasdsad asdasdasd')
count = 0
for i in s:
   if i == "a":
       count += 1
print(count)