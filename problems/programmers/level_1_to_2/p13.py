# 카펫

def solution(brown, yellow):
    answer = []
    for w in range(yellow, 0, -1):
        if yellow % w == 0:
            h = yellow // w
            if 2 * w + 2 * h + 4 == brown:
                answer.append(w+2)
                answer.append(h+2)
                break
    return answer


if __name__ == '__main__':
    print(solution(24, 24))
