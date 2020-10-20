def check(x):
    cnt = 1
    ept = a[0]
    for i in range(len(a)):
        if a[i] - ept >= x:
            cnt += 1
            ept = a[i]
    return cnt


if __name__ == '__main__':
    n, c = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    a.sort()
    lt = 1
    rt = a[-1]
    res = 0

    while lt <= rt:
        mid = (lt + rt) // 2
        if check(mid) >= c:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1

    print(res)