if __name__ == '__main__':
    s = input()
    stack = []

    for c in s:
        if c.isdecimal():
            stack.append(int(c))
        else:
            b = stack.pop()
            a = stack.pop()

            if c == '*':
                stack.append(a*b)
            elif c == '/':
                stack.append(a/b)
            elif c == '+':
                stack.append(a+b)
            elif c == '-':
                stack.append(a-b)

    print(stack[0])
