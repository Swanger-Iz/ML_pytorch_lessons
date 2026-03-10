from inspect import getgeneratorstate

# Делегирующий генератор - это генератор, который вызывает какой-нибудь другой
# подгенератор - это вызываемый генератор


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class BlaBlaExp(Exception): ...


def subgen():
    while 1:
        try:
            message = yield
        except StopIteration:
            # print("Ku-ku!!")
            break
        else:
            print("." * 10, message)

    return "Returned from subgen()"


@coroutine
def delegator(g):
    # while 1:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaExp as e:
    #         g.throw(e)
    result = yield from g
    print(result)


sg = subgen()
g = delegator(sg)

g.send("OK")
