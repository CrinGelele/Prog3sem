import sys


def get_num(x, request):
    try:
        num = sys.argv[x]
    except:
        print(request, end=' ')
        num = input()
    while True:
        try:
            num = float(num)
            break
        except:
            print('Неверный формат, введите заново:', end=' ')
            num = input()
    return num


def solve(a, b, c):
    d = b * b - (4 * a * c)
    ans = []
    tentative = []
    if a != 0:
        if d > 0:
            d = d ** 0.5
            tentative.append((d - b) / (2 * a))
            tentative.append((-d - b) / (2 * a))
            for i in tentative:
                if i > 0:
                    tmp = i ** 0.5
                    ans.append(tmp)
                    ans.append(-tmp)
                elif i == 0:
                    ans.append(0)
        elif d == 0:
            ans.append(0)
    else:
        if c < 0 and b > 0 or c > 0 and b < 0:
            tmp = (abs(c) / abs(b)) ** 0.5
            ans.append(tmp)
            ans.append(-tmp)
        elif c == 0:
            ans.append(0)
    return ans


def main():
    a = get_num(1, 'Введите коэффициент А:')
    b = get_num(2, 'Введите коэффициент B:')
    c = get_num(3, 'Введите коэффициент C:')
    ans = list(map(str, sorted(solve(a, b, c))))
    if len(ans) == 0:
        print('Нет корней')
    else:
        print('Получено', len(ans), 'корней:', ', '.join(ans))


if __name__ == "__main__":
    main()
