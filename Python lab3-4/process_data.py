import json
from print_result import print_result
from cm_timer import cm_timer1
from gen_random import gen_random
from unique import Unique
from field import field

path = 'D:\GitRepos\Proga3sem\Python lab3-4\data_light.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted([x for x in Unique(field(arg, 'job-name'), ignore_case=True)])


@print_result
def f2(arg):
    return list(filter(lambda x: 'Программист' == x.split()[0], arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    return [str(i) + ', зарплата ' + str(j) + ' руб.' for i, j in zip(arg, gen_random(len(arg), 100000, 200000))]


if __name__ == '__main__':
    with cm_timer1():
        f4(f3(f2(f1(data))))