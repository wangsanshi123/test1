def f(x, y):
    return x * y


def test1():
    return reduce(f, [1, 3, 5, 7, 9])


if __name__ == '__main__':
    print(test1())
