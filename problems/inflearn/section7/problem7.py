from collections import deque

if __name__ == '__main__':
    s, e = map(int, input().split())
    d = [0] * 10001
    ch = [0] * 10001
    q = deque()
    d[s] = 0
    ch[s] = 1
    q.append(s)
    while True:
        v = q.popleft()
        if v == e:
            break
        if 1 <= v-1 <= 10000 and not ch[v-1]:
            d[v-1] = d[v] + 1
            ch[v-1] = 1
            q.append(v-1)
        if 1 <= v+1 <= 10000 and not ch[v+1]:
            d[v+1] = d[v] + 1
            ch[v+1] = 1
            q.append(v+1)
        if 1 <= v+5 <= 10000 and not ch[v+5]:
            d[v+5] = d[v] + 1
            ch[v+5] = 1
            q.append(v+5)
    print(d[e])
