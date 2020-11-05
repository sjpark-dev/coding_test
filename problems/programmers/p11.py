# 행렬의 곱셈

def solution(arr1, arr2):
    m = len(arr1)
    n = len(arr2[0])
    a = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            sum = 0
            for k in range(len(arr1[0])):
                sum += arr1[i][k] * arr2[k][j]
            a[i][j] = sum
    return a


if __name__ == '__main__':
    print(solution([[1, 2, 3], [4, 5, 6]],  [[1, 4], [2, 5], [3, 6]]))
