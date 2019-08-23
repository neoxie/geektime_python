x = 1

def foo():
    global x
    print(x)
    x = 10


foo()  # UnboundLocalError: local variable 'x' referenced before assignment
