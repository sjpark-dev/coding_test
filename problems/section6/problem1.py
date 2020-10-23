def base2(x):
    return x if x == 1 or x == 0 else str(base2(x//2)) + str(x%2)


if __name__ == '__main__':
    n = int(input())
    print(base2(n))
