if __name__ == '__main__':
    word1 = input()
    d = {}

    for c in word1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    word2 = input()

    for c in word2:
        if c in d:
            d[c] -= 1

    for v in d.values():
        if v != 0:
            print('NO')
            break
    else:
        print('YES')
