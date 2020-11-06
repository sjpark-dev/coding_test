# N개의 최소공배수

import math


def solution(arr):
    while len(arr) >= 2:
        a = arr.pop()
        b = arr.pop()
        arr.append(lcm(a, b))
    answer = arr[0]
    return answer


def lcm(a, b):
    gcd = math.gcd(a, b)
    return a * b // gcd


if __name__ == '__main__':
    print(solution([1,2,3]))
