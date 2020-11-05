def prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# 사용 예시
if __name__ == '__main__':
    # 1부터 100까지의 소수 출력
    for i in range(1, 101):
        if prime(i):
            print(i, end=' ')
