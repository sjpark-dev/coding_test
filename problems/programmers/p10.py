def solution(s):
    s = s.lower()
    s = list(s)
    for i in range(len(s)):
        if i == 0:
            s[i] = s[i].upper()
        if i != 0 and s[i-1] == ' ':
            s[i] = s[i].upper()
    answer = ''.join(s)
    return answer


if __name__ == '__main__':
    print(solution('3people unFollowed me'))
