if __name__ == '__main__':
    n = int(input())
    meetings = []

    for _ in range(n):
        s, e = map(int, input().split())
        meetings.append((s,e))

    meetings.sort(key=lambda x: (x[1], x[0]))
    cnt = 0
    et = 0

    for meeting in meetings:
        if meeting[0] >= et:
            cnt += 1
            et = meeting[1]

    print(cnt)
