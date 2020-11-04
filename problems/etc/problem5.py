n = int(input())
cnt = 0

for i in range(1, n+1):
    tmp = list(str(i))
    for t in tmp:
        if t == '3' or t == '6' or t == '9':
            cnt += 1

print(cnt)
