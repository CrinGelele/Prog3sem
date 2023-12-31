def print_result(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        print(func.__name__)
        if isinstance(a, list):
            for i in a:
                print(i)
        elif isinstance(a, dict):
            for key, value in a.items():
                print(key, ' = ', value)
        else:
            print(a)
        return a
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
