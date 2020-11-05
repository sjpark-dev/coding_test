# 최솟값 만들기

def solution(A,B):
    A.sort()
    B.sort()
    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[len(B)-1-i]
    return answer


if __name__ == '__main__':
    print(solution([1, 2], [3, 4]))
