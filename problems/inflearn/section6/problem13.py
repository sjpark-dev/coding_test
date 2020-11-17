def dfs(l):
    global cnt
    res.append(l)
    for i in range(1, n+1):
        if matrix[l][i] == 1 and i not in res:
            if i == n:
                cnt += 1
            else:
                dfs(i)
    res.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        matrix[a][b] = 1
    res = []
    cnt = 0
    dfs(1)
    print(cnt)
