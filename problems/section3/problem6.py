n = int(input())
board = []

for i in range(n):
    board.append(list(map(int, input().split())))

max_sum = 0
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

for i in range(n):
    sum1 = 0
    sum2 = 0

    for j in range(n):
        sum1 += board[i][j]
        sum2 += board[j][i]

    max_sum = max(max_sum, sum1, sum2)
    sum3 += board[i][i]
    sum4 += board[n-1-i][i]

max_sum = max(max_sum, sum3, sum4)
print(max_sum)
