import sys


def dfs(l):
    if l == n:
        if triangle() == f:
            print(*a)
            sys.exit(0)
    else:
        for i in range(1, n+1):
            if check[i] == 1:
                continue
            check[i] = 1
            a[l] = i
            dfs(l+1)
            check[i] = 0


def triangle():
    b = a.copy()
    for _ in range(n-1):
        temp = []
        for i in range(len(b)-1):
            temp.append(b[i]+b[i+1])
        b = temp
    return b[0]


if __name__ == '__main__':
    n, f = map(int, input().split())
    a = [0] * n
    check = [0] * (n + 1)
    dfs(0)
