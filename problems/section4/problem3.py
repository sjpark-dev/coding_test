def size(n):
    cnt = 1
    sum = 0
    for x in a:
        if sum + x > n:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


n, m = map(int, input().split())
a = list(map(int, input().split()))
maxx = max(a)
lt = 1
rt = sum(a)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= maxx and size(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
