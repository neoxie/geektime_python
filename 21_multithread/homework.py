import time
import concurrent.futures
import threading
import multiprocessing


def cpu_bound(number):
    print(sum(i * i for i in range(number)))


def calculate_sums(numbers):
    # for number in numbers: #1 single thread
    #     cpu_bound(number)  #1 single thread
    # with concurrent.futures.ProcessPoolExecutor() as executor: #2 multi-process
    #     executor.map(cpu_bound, numbers) #2 multi-process
    with multiprocessing.Pool() as pool: #3 multiprocessing pool
        pool.map(cpu_bound, numbers)  #3 multiprocessing pool


def main():
    start_time = time.perf_counter()
    numbers = [10000000 + x for x in range(20)]
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))


if __name__ == '__main__':
    main()
