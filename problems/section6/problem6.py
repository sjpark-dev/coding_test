from itertools import product

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(range(1, n+1))
    a = list(product(a, repeat=m))
    for x in a:
        for y in x:
            print(y, end=' ')
        print()
    print(len(a))
