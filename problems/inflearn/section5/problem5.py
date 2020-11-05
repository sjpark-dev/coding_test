from collections import deque

if __name__ == '__main__':
    n, k = map(int, input().split())
    q = deque(range(1, n+1))

    while len(q) > 1:
        for i in range(k-1):
            q.append(q.popleft())
        q.popleft()

    print(q[0])
