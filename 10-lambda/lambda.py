from functools import reduce
l1 = [(lambda x: x * x)(x) for x in range(10)]
print(l1)
# 输出
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1])  # 按列表中元祖的第二个元素排序
print(l)
# 输出s
# [(2, -1), (3, 0), (9, 10), (1, 20)]

numbers = (1, 2, 3, 4, 5, 6)
result = map(lambda x: x * 2, numbers)
print(list(result))

l = (1, 2, 3, 4, 5, 6)
new_list = filter(lambda x: x % 2 == 0, l)  # [2, 4]
print(set(new_list))

l = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, l)  # 1*2*3*4*5 = 120
print(product)
