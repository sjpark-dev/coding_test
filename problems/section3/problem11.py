def check(n):
    for i in range(2):
        if n[i] != n[-1 - i]:
            return False
    return True


board = [list(map(int, input().split())) for i in range(7)]
cnt = 0

for i in range(7):
    for j in range(3):
        tmp = board[i][j:j + 5]

        if tmp == tmp[::-1]:
            cnt += 1

        for k in range(2):
            if board[j + k][i] != board[j + 5 - k - 1][i]:
                break
        else:
            cnt += 1

print(cnt)
