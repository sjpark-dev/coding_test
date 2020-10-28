import sys


def dfs(l, sum):
    if sum > total // 2:  # 시간 복잡도를 줄이기 위한 코드
        return
    if l == n:
        if sum == total-sum:
            print('YES')
            sys.exit(0)
    else:
        dfs(l+1, sum+a[l])
        dfs(l+1, sum)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    dfs(0, 0)
    print('NO')