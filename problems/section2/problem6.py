def digit_sum(x):
    sum = 0

    while x:
        sum += x % 10
        x = x // 10
    return sum


n = int(input())
nums = list(map(int, input().split()))
max = 0

for a in nums:
    ds = digit_sum(a)
    if ds > max:
        max = ds
        ans = a

print(ans)