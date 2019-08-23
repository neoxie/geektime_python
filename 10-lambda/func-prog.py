def multiply_2(l):
    for index in range(0, len(l)):
        l[index] *= 2
    return l

l = [1,2,3,4,5]
multiply_2(l)
print(l)
multiply_2(l)
print(l)
