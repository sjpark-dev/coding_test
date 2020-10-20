n = int(input())
ans = 0

for i in range(n):
    numbers = input().split()
    numbers.sort()
    a, b, c = map(int, numbers)

    if a == b and b == c:
        money = 10000 + 1000 * a
    elif a == b or  a == c:
        money = 1000 + 100 * a
    elif b == c:
        money = 1000 + 100 * b
    else:
        money = 100 * c

    if ans < money:
        ans = money

print(ans)