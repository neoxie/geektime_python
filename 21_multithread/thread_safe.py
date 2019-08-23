import threading

n = 0


def foo():
    global n
    n += 1


def main():
    threads = []
    for i in range(1000):
        t = threading.Thread(target=foo)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    for value in range(1000):
        main()
        print(n)
        n = 0
