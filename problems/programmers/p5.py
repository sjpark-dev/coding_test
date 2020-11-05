# 큰 수 만들기

def solution(number, k):
    number = list(map(int, list(number)))
    stack = []
    for x in number:
        while stack and k > 0 and stack[-1] < x:
            stack.pop()
            k -= 1
        stack.append(x)
    if k != 0:
        stack = stack[:-k]
    answer = ''.join(map(str, stack))
    return answer


if __name__ == '__main__':
    print(solution('4177252841', 4))
