def base_10_to_base_n(base_n, number):
    result = 0
    i = 1
    while number > 0:
        temp = number % base_n
        result += temp * i
        number //= base_n
        i *= 10
    return result


# 사용 예시
if __name__ == '__main__':
    # 10진수 11을 2진수로 변환
    n = base_10_to_base_n(2, 11)
    print(n)  # 1011
