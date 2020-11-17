if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [[0] * n for _ in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        matrix[a-1][b-1] = w
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()
