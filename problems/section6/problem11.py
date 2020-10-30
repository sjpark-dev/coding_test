def dfs(l,s):
    global cnt
    if l == k:
        if sum(p) % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            p[l] = a[i]
            dfs(l+1, i+1)


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    p = [0] * k
    cnt = 0
    dfs(0, 0)
    print(cnt)
