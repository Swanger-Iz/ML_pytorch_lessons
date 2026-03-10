from inspect import getgeneratorstate


def subgen():
    x = "Ready to accept message"
    message = yield x
    print("Subgen received:", message)


class BlaBlaExp(Exception): ...


def couroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


# avrage = couroutine(average)


@couroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except BlaBlaExp:
            print("-" * 20)
            break
        except StopIteration:
            print("done")
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
    return average
