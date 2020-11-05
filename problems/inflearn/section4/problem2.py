def count(n):
    cnt = 0
    for x in a:
        cnt += x // n
    return cnt


k, n = map(int, input().split())
a = []

for i in range(k):
    a.append(int(input()))

lt = 1
rt = max(a)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
