x = 1


def foo(x):
    print(x)
    x = 2
    print(x)


foo(x)
print(x)  # 1
