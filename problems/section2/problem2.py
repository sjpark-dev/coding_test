t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers = numbers[s-1:e]
    numbers.sort()
    print('#{} {}'.format(i+1, numbers[k-1]))
