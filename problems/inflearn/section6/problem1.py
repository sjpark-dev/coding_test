def base2(x):
    if x == 0:
        return
    else:
        base2(x//2)
        print(x % 2, end='')


if __name__ == '__main__':
    n = int(input())
    base2(n)
