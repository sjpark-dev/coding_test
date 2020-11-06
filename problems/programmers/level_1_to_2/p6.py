# H-Index

def solution(citations):
    citations.sort()
    answer = 0
    for i in range(len(citations), -1, -1):
        if count(citations, i) >= i:
            answer = i
            break
    return answer


def count(a, h):
    cnt = 0
    for x in a:
        if x >= h:
            cnt += 1
    return cnt


if __name__ == '__main__':
    print(solution([33, 66]))
