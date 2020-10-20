n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))
i1 = i2 = 0
list3 = []
while i1 < n and i2 < m:
    if list1[i1] < list2[i2]:
        list3.append(list1[i1])
        i1 += 1
    else:
        list3.append(list2[i2])
        i2 += 1

if i1 < n:
    list3 = list3 + list1[i1:]

if i2 < m:
    list3 = list3 + list2[i2:]

print(*list3)