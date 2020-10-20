def get_num(s):
    nums = '0123456789'
    n = 0
    for c in s:
        if c in nums:
            n = 10 * n + int(c)
    return n

def num_div(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt

s = input()
n = get_num(s)
print(n)
n = num_div(n)
print(n)