p = list(map(int, input().split()))
c = list(map(int, input().split()))


def f(n):
    s1 = 0
    s2 = 1
    while n:
        s1 += n % 10
        s2 *= n % 10
        n = n // 10
    if s2 > s1:
        return s2
    else:
        return s1


if p[0] % 2 != 1 or c[0] % 2 != 1 or p[1] % 2 != 0 or c[1] % 2 != 0 or p[1] - p[0] != 1 or c[1] - c[0] != 1:
    print(-1)
elif not (1 <= p[0] <= 400) or not (1 <= p[1] <= 400) or not (1 <= c[0] <= 400) or not (1 <= c[1] <= 400):
    print(-1)
else:
    if max(f(p[0]), f(p[1])) > max(f(c[0]), f(c[1])):
        print(1)
    elif max(f(p[0]), f(p[1])) < max(f(c[0]), f(c[1])):
        print(2)
    else:
        print(0)
