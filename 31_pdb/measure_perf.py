import cProfile
# def fib(n)
# def fib_seq(n):


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n - 1))
    res.append(fib(n))
    return res


# r = fib_seq(30)
# print(r)

# python3 -m cProfile xxx.py
# https://docs.python.org/3.7/library/profile.html

cProfile.run('fib_seq(30)')
