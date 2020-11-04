word = input()
res = ''

for char in word:
    a = ord(char)
    if 97 <= a <= 122:
        a = 122 - (a - 97)
    elif 65 <= a <= 90:
        a = 90 - (a - 65)
    res += chr(a)

print(res)
