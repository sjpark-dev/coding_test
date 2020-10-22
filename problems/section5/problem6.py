from collections import deque

if __name__ == '__main__':
    n, m = map(int, input().split())
    q = deque([(p, v) for p, v in enumerate(map(int, input().split()))])
    cnt = 0

    while True:
        cur = q.popleft()

        if any(cur[1] < x[1] for x in q):
            q.append(cur)
        else:
            cnt += 1

            if cur[0] == m:
                print(cnt)
                break
