n = int(input())
prime = [1] * (n+1)
ans = 0

for i in range(2, n+1):
    if prime[i]:
        ans += 1
        for j in range(i*2, n+1, i):
            prime[j] = 0

print(ans)