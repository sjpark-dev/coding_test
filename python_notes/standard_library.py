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
a = list(product(a, repeat=2))  # [(1, 2), (1, 3), (2, 3)] (repeat 속성 필요)
# 조합 (중복 허용)
a = [1, 2, 3]
a = list(combinations_with_replacement(a, 2))  # [(1, 2), (1, 3), (2, 3)]
# permuatations, combinations, product, combinations_with_replacement는 클래스이므로 초기화 이후 리스트 자료형으로 변환
print(a)

# heapq
