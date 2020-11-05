def dfs(l, tsum):
    global result
    if sum(a) > result:
        return
    if l == n:
        total = 0
        for i in range(n):
            total += coins[i] * a[i]
        if total == m and sum(a) < result:
            result = sum(a)
    else:
        for i in range(tsum//coins[l]+1):
            a[l] = i
            dfs(l+1, tsum-(coins[l]*i))
            a[l] = 0


if __name__ == '__main__':
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    a = [0] * n
    result = 500
    dfs(0, m)
    print(result)
