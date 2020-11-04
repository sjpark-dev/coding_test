t = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
money = int(input())
res = [0] * 9

for i in range(len(t)):
    res[i] = money // t[i]
    money = money % t[i]

print(res)
