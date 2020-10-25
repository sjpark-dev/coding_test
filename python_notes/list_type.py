""" 리스트 자료형 """

# 빈 리스트 선언
a = list()  # 방법1
a = []  # 방법 2

# 리스트를 0으로 초기화
a = [0] * 10  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 인덱싱
a = list(range(1, 10))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[-1]  # 9 (뒤에서 첫번째 원소)
# 슬라이싱
b = a[1:4]  # [2, 3, 4]
b = a[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1] (역순 리스트)

# 리스트 컴프리헨션
a = [i for i in range(20) if i % 2 == 1]  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# 아래 코드와 같다
# a = []
# for i in range(20):
#     if i % 2 == 1:
#         a.append(i)
a = [i * i for i in range(1, 10)]  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 아래 코드와 같다
# a = []
# for i in range(1, 10):
#     a.append(i * i)

# n x m 크기의 2차원 리스트 초기화
n = 3
m = 4
a = [[0] * m for _ in range(n)]  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# .append(element) O(1)
# .pop() O(1)
# .sort() O(NlogN)
# .reverse() O(N)
# .count(element) O(N)
# .insert(index, element) O(N)
# .remove(element) O(N) (같은 값을 가진 원소가 여러 개면 하나만 제거)
# 특정한 값의 원소 모두 제거하는 코드
a = [1, 2, 3, 4, 5, 5, 5]
b = {3, 5}
a = [i for i in a if i not in b]  # [1, 2, 4]
