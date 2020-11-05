# 이해가 잘 안됨, 나중에 한번더 볼 것

if __name__ == '__main__':
    n = int(input())
    body = []

    for i in range(n):
        a, b = map(int, input().split())
        body.append((a, b))

    body.sort(reverse=True)
    largest = 0
    cnt = 0

    for x, y in body:
        if y > largest:
            largest = y
            cnt += 1

    print(cnt)
