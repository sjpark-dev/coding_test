from collections import deque

if __name__ == '__main__':
    n, m = map(int, input().split())
    q = deque(zip(map(int, input().split()), range(n)))
    cnt = 0

    while True:
        for i in range(1, len(q)):
            if q[0][0] < q[i][0]:
                q.append(q.popleft())
        else:
            p = q.popleft()
            cnt += 1

            if p[1] == m:
                print(cnt)
                break
