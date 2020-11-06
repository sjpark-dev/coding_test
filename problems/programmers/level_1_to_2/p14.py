# 타겟 넘버

def solution(numbers, target):
    answer = dfs(0, numbers, 0, target)
    return answer


def dfs(l, a, total, target):
    if l == len(a):
        if total == target:
            return 1
        else:
            return 0
    else:
        return dfs(l+1, a, total+a[l], target) + dfs(l+1, a, total-a[l], target)


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))
