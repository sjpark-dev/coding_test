def solution(s):
    answer = True
    stack = []
    for x in s:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True if len(stack) == 0 else False


if __name__ == '__main__':
    print(solution('(()('))
