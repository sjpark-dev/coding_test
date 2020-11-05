""" 표줌 라이브러리 """

'''
- 내장 함수
- itertools
- heapq
- bisect
- collections
- math
'''

'''
내장 함수
sum()
min()
max()
eval()  # 문자열 형식의 수식을 계산 결과를 반환
    ex) print(eval('(1 + 2) * 3'))  # 9
sorted()
    reverse(True/False), key(len/lambda...) 속성 사용 가능
chr()
ord()
all()
any()
'''

# itertools
from itertools import permutations, combinations, product, combinations_with_replacement

# 순열
a = [1, 2, 3]
a = list(permutations(a, 3))  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# 조합
a = [1, 2, 3]
a = list(combinations(a, 2))  # [(1, 2), (1, 3), (2, 3)]
# 순열 (중복 허용)
a = [1, 2, 3]
a = list(product(a, repeat=2))  # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)] (repeat 필요)
# 조합 (중복 허용)
a = [1, 2, 3]
a = list(combinations_with_replacement(a, 2))  # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
# permuatations, combinations, product, combinations_with_replacement는 클래스이므로 초기화 이후 리스트 자료형으로 변환
print(a)

# heapq
import heapq

# 최소 힙
h = []
v = 1
heapq.heappush(h, v)
a = heapq.heappop(h)

# 최대 힙
h = []
v = 1
heapq.heappush(h, -v)
a = -heapq.heappop(h)

# bisect
from bisect import bisect_left, bisect_right

a = [1, 2, 3, 3, 4, 5]
x = 3
print(bisect_left(a, x))  # 2 (정렬된 리스트에서 x를 삽입할 가장 왼쪽 인덱스를 반환)
print(bisect_right(a, x))  # 4 (정렬된 리스트에서 x를 삽입할 가장 오른쪽 인덱스를 반환)
# 정렬된 리스트에서 left_value <= x <= right_value인 x의 개수를 찾을때 사용 가능, O(logN)

# collections
from collections import deque, Counter

# 덱
a = deque()
# deque는 슬라이싱 안됨, 인덱싱은 됨.
# .append(element), .appendleft(element)
# .pop(), .popleft()

# 카운터
a = Counter([1, 1, 2, 2, 2, 3, 3, 3])  # Counter(iterable)
print(a[1])  # 2
print(a[2])  # 3
print(a[3])  # 3
print(dict(a))  # {1: 2, 2: 3, 3: 3} (사전 자료형으로 변환)

# math
import math

# 팩토리얼
print(math.factorial(5))  # 120

# 제곱근
print(math.sqrt(49))  # 7.0

# 최대공햑수
print(math.gcd(21, 14))  # 7

# pi, e
print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045
