a = 1
b = a
print(id(a))
print(id(b))
a += 1
print(id(a))
print(id(b))
print('================')
l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l2
print(id(l1))
print(id(l2))
print(id(l3))

print('=================')


def func(dd):
    dd['a'] = 10
    dd['b'] = 20


d1 = {'a': 1, 'b': 2}
func(d1)
print(d1)
