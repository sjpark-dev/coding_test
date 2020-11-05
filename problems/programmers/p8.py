import math


def solution(n, m):
    # x = gcd(n,m)
    x = math.gcd(n, m)
    y = n * m // x
    answer = [x, y]
    return answer


# def gcd(n, m):
#     n_set = set()
#     m_set = set()
#     for i in range(1, n+1):
#         if n % i == 0:
#             n_set.add(i)
#     for i in range(1, m+1):
#         if m % i == 0:
#             m_set.add(i)
#     cd = n_set & m_set
#     return max(cd)


if __name__ == '__main__':
    print(solution(2, 5))
