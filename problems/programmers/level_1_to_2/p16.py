# 다음 큰 숫자

def solution(n):
    answer = n
    n_one_cnt = bin(n)[2:].count('1')
    while True:
        answer += 1
        if bin(answer)[2:].count('1') == n_one_cnt:
            break
    return answer


if __name__ == '__main__':
    print(solution(15))
