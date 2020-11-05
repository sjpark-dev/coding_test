n = int(input())
map1 = []
map1.append([0] * (n+2))

for i in range(n):
    map1.append([0] + list(map(int, input().split())) + [0])

map1.append([0] * (n+2))
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(map1[i][j] > map1[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
