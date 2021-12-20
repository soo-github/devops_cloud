
def base_10(fn):
    def wrap(x, y):
        return fn(x, y) + 10
    return wrap


@base_10
@base_10
def mysum(x, y):
    return x + y


print(mysum(1, 2))
