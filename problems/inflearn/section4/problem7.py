if __name__ == '__main__':
    l = int(input())
    warehouse = list(map(int, input().split()))
    m = int(input())

    for i in range(m):
        warehouse.sort()
        warehouse[-1] -= 1
        warehouse[0] += 1

    warehouse.sort()
    print(warehouse[-1] - warehouse[0])
