import time
import functools


def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res

    return wrapper


@log_execution_time
def calculate_similarity():
    count = 0
    for value in range(1, 100000000):
        count += value
    return count


c = calculate_similarity()
print(c)
