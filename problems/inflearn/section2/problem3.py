n, k = map(int, input().split())
nums = list(map(int, input().split()))
sum_set = set()
for a in range(n-2):
    for b in range(a+1, n-1):
        for c in range(b+1, n):
            sum_set.add(nums[a] + nums[b] + nums[c])

sum_list = list(sum_set)
sum_list.sort(reverse=True)
print(sum_list[k-1])
