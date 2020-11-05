n = int(input())
for i in range(n):
    word = input()
    word = word.upper()
    for j in range(len(word)//2):
        if word[j] != word[len(word)-(1+j)]:
            print('#{} NO'.format(i + 1))
            break
    else:
        print('#{} YES'.format(i+1))
