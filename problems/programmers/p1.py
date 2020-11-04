# 조이스틱

def solution(name):
    name = list(name)
    answer = 0
    p = 0
    s = ['A'] * len(name)
    while True:
        if ''.join(name) == ''.join(s):
            break
        if name[p] != s[p]:
            answer += check_up_down(name[p])
            name[p] = 'A'
        else:
            tmp = check_left_right(p, name)
            answer += tmp[0]
            p = tmp[1]
    return answer


def check_up_down(x):
    if ord(x) <= ord('M'):
        return ord(x) - 65
    else:
        return 91 - ord(x)


def check_left_right(x, a):
    up = x
    up_count = 0
    down = x
    down_count = 0
    while True:
        up += 1
        up_count += 1
        if up == len(a):
            up -= len(a)
        if a[up] != 'A':
            break
    while True:
        down -= 1
        down_count += 1
        if down == -1:
            down += len(a)
        if a[down] != 'A':
            break
    if up_count <= down_count:
        return up_count, up
    else:
        return down_count, down


if __name__ == '__main__':
    problem_input = input()
    print(solution(problem_input))
