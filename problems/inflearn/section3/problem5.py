n, m = map(int, input().split())
seq = list(map(int, input().split()))
cnt = 0
total = seq[0]
lt = 0
rt = 1

while True:
    if total < m:
        if rt < n:
            total += seq[rt]
            rt += 1
        else:
            break
    elif total == m:
        cnt += 1
        total -= seq[lt]
        lt += 1
    else:
        total -= seq[lt]
        lt += 1

print(cnt)