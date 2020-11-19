def dfs(l, score, time):
    global max_score
    if l == n:
        if time <= m:
            if score > max_score:
                max_score = score
    else:
        dfs(l+1, score + data[l][0], time + data[l][1])
        dfs(l+1, score, time)


if __name__ == '__main__':
    n, m = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(tuple(map(int, input().split())))
    max_score = 0
    dfs(0, 0, 0)
    print(max_score)
