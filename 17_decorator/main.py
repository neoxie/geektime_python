def my_decorator(func):
    def wrapper(msg):
        print('wrapper of decorator')
        func(msg)

    return wrapper


@my_decorator
def greet(msg):
    print(msg)


greet('hello world')
