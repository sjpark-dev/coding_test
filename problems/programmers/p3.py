# 소수 찾기

from itertools import permutations


def solution(numbers):
    a = list(numbers)
    ch = [0] * len(a)
    p = []
    dfs(0, a, ch, p)
    s = set()
    for x in p:
        s.add(int(''.join(x)))
    answer = 0
    for x in s:
        if prime(x):
            answer += 1
    return answer


def dfs(l, a, ch, p):
    if l == len(a):
        b = []
        for i in range(len(ch)):
            if ch[i] == 1:
              b.append(a[i])
        if len(b) != 0:
            p = p.extend(list(permutations(b, len(b))))
    else:
        ch[l] = 1
        dfs(l+1, a, ch, p)
        ch[l] = 0
        dfs(l+1, a, ch, p)


def prime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


if __name__ == '__main__':
    print(solution('011'))
