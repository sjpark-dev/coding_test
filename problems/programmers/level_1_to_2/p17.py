# 숫자의 표현

def solution(n):
    a = 1
    b = 1
    cnt = 0
    while a <= b:
        total = b * (b + 1) // 2 - (a-1) * a // 2
        if total >= n:
            if total == n:
                cnt += 1
            a += 1
        else:
            b += 1
    return cnt


if __name__ == '__main__':
    print(solution(15))
