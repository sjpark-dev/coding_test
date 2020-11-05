def dfs(l):
    global cnt
    if l == m:
        print(*b)
        cnt += 1
    else:
        for i in range(1, n+1):
            if a[i] == 1:
                continue
            a[i] = 1
            b[l] = i
            dfs(l+1)
            a[i] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * (n+1)
    b = [0] * m
    cnt = 0
    dfs(0)
    print(cnt)
