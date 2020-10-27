def dfs(x):
    global i
    if x == n:
        sum = 0
        for i in range(n):
            if check[i] == 1:
                sum += a[i]
            else:
                sum -= a[i]
        if sum == 0:
            pos[i] = 1
        i += 1
        return
    else:
        check[x] = 1
        dfs(x+1)
        check[x] = 0
        dfs(x+1)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    check = [0] * n
    pos = [0] * (2**n)
    i = 0
    dfs(0)

    if any(i for i in pos):
        print('YES')
    else:
        print('NO')
