def reverse(x):
    ans = 0
    while x:
        tmp = x % 10
        ans = ans * 10 + tmp
        x = x // 10
    return ans


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


n = int(input())
nums = list(map(int, input().split()))
for num in nums:
    rnum = reverse(num)
    if isPrime(rnum):
        print(rnum, end=' ')
