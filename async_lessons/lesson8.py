import time

queue = []


def counter():
    counter = 0
    while 1:
        print(counter)
        counter += 1
        yield


def printer():
    counter = 0

    while 1:
        if counter % 3 == 0:
            print("bang")
        counter += 1
        yield


def main():
    while 1:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        time.sleep(0.5)


if __name__ == "__main__":
    g1 = counter()
    g2 = printer()
    queue.extend([g1, g2])
    print(queue)
    main()
