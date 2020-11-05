n = int(input())
li = list(map(int, input().split()))
avg = int(sum(li) / n + 0.5)
min = abs(li[0]-avg)
stu = 0
score = li[0]

for i, x in enumerate(li):
    gap = abs(x-avg)
    if min > gap:
        min = gap
        score = x
        stu = i + 1
    elif min == gap:
        if x > score:
            score = x
            stu = i + 1

print(avg, stu)
