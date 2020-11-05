from collections import deque

if __name__ == '__main__':
    order = input()
    n = int(input())

    for i in range(n):
        o = deque(order)
        s = input()

        for x in s:
            if x in o:
                if x != o.popleft():
                    print(f'#{i+1} NO')
                    break

            if len(o) == 0:
                print(f'#{i+1} YES')
                break
        else:
            print(f'#{i+1} NO')
