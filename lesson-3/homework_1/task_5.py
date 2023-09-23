list_a = [1, 2, 3]
list_a.append('four')
list_a[1] = 'two'
print(list_a)
set_b = {5, 6}
list_a.append(set_b)
set_b.add(7)
tuple_c = (2.5, 2.6)
list_a.insert(2, tuple_c)
print(list_a)