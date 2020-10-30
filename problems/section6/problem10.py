def dfs(l, s):
    global cnt
    if l == m:
        print(*a)
        cnt += 1
    else:
        for i in range(s, n+1):
            a[l] = i
            dfs(l+1, i+1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * m
    cnt = 0
    dfs(0, 1)
    print(cnt)
