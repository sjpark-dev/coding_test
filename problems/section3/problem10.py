def check_sudoku(sudoku):
    for i in range(9):
        check1 = [0] * 10
        check2 = [0] * 10
        for j in range(9):
            check1[sudoku[i][j]] = 1
            check2[sudoku[j][i]] = 1
        if sum(check1) != 9 or sum(check2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            check3 = [0] * 10
            for k in range(3):
                for l in range(3):
                    check3[sudoku[i * 3 + k][j * 3 + l]] = 1
            if sum(check3) != 9:
                return False
    return True


sudoku = [list(map(int, input().split())) for i in range(9)]
if check_sudoku(sudoku):
    print('YES')
else:
    print('NO')
