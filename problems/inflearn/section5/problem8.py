if __name__ == '__main__':
    n = int(input())
    d = {}

    for i in range(n):
        d[input()] = 1

    for i in range(n-1):
        d[input()] -= 1

    for k in d.keys():
        if d[k] == 1:
            print(k)
            break
