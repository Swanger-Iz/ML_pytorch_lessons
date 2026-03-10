from time import time


def gen_filename():
    while True:
        pattern = "filename{}.jpeg"
        t = time() * 1000
        yield pattern.format(str(t))

        sum = 222 + 100
        yield sum


def gen(name):
    for i in name:
        yield i


def gen2(n):
    for i in n:
        yield i


g1 = gen2("Oleg")
g2 = gen2("Ilgiz")

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        ...
