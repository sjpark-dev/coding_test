# 체육복

def solution(n, lost, reserve):
    a = [0] + [1] * n
    for x in lost:
        a[x] -= 1
    for x in reserve:
        a[x] += 1
    for i in range(1, n+1):
        if a[i] == 0:
            if a[i-1] == 2:
                a[i-1] -= 1
                a[i] += 1
            elif i != n and a[i+1] == 2:
                a[i+1] -= 1
                a[i] += 1
    answer = 0
    for x in a:
        if x != 0:
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution(3, [3], [1]))
