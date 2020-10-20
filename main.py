if __name__ == '__main__':
    a = [5,1,2,7,8,2,1]
    b = []
    m = 5

    for x in a:
        while b and x > b[-1] and m > 0:
            b.pop()
            m -= 1
        b.append(x)

    if m != 0:
        b = b[:-m]

    print(b)