cryptogram = input()

while True:
    cnt = 0
    res = ''
    for i in range(len(cryptogram)):
        if i != len(cryptogram)-1 and cryptogram[i] == cryptogram[i+1]:
            cnt += 1
            continue
        elif i != 0 and cryptogram[i] == cryptogram[i-1]:
            cnt += 1
            continue
        else:
            res += cryptogram[i]
    cryptogram = res
    if cnt == 0:
        break

print(cryptogram)
