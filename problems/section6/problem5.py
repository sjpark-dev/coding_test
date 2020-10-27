def dfs(x):
    global total
    if x == n:
        sum = 0
        for i in range(n):
            if check[i] == 1:
                sum += a[i]
        if total < sum <= c:
            total = sum
        return
    else:
        check[x] = 1
        dfs(x+1)
        check[x] = 0
        dfs(x+1)


if __name__ == '__main__':
    c, n = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    check = [0] * n
    total = 0
    dfs(0)
    print(total)
