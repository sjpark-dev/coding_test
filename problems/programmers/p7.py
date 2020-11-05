from collections import deque


def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0
    while people:
        if len(people) == 1:
            answer += 1
            break
        else:
            if people[0] + people[-1] <= limit:
                people.popleft()
                people.pop()
                answer += 1
            else:
                people.pop()
                answer += 1
    return answer


if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100))
