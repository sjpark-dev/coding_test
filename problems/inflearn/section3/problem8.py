n = int(input())
space = [list(map(int, input().split())) for i in range(n)]
cn = int(input())

for i in range(cn):
    a, b, c = map(int, input().split())
    if b:
        for j in range(c):
            space[a-1].insert(0, space[a-1].pop())
    else:
        for j in range(c):
            space[a-1].append(space[a-1].pop(0))

s, e = 0, n-1
sum = 0

for i in range(n):
    for j in range(s, e+1):
        sum += space[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(sum)
