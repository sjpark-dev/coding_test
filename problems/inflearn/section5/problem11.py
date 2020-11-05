import heapq

if __name__ == '__main__':
    heap = []

    while True:
        n = int(input())

        if n == -1:
            break

        if n == 0:
            if len(heap) == 0:
                print(-1)
            else:
                print(-heapq.heappop(heap))
            continue

        heapq.heappush(heap, -n)
