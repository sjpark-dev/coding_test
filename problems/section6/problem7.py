def dfs(l, sum):
    global result
    if l == n:
        total = 0
        for i in range(n):
            total += coins[i] * a[i]
        if total == m and sum(a) < result:
            result = sum(a)
    else:
        for i in range(sum//coins[l]+1):
            a[l] = i
            dfs(l+1, sum-(coins[l]*i))


if __name__ == '__main__':
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    a = [0] * n
    result = 500
    dfs(0, m)
    print(result)
