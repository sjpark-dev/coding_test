def base_n_to_base_10(base_n, number):
    result = 0
    i = 1
    while number > 0:
        temp = number % 10
        result += temp * i
        number //= 10
        i *= base_n
    return result


# 사용 예시
if __name__ == '__main__':
    # 2진수 1011을 10진수로 변환
    n = base_n_to_base_10(2, 1011)
    print(n)  # 11
