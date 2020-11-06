# 더 맵게

import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        if scoville[0] >= K:
            break
        if len(scoville) == 1:
            answer = -1
            break
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12], 7))
