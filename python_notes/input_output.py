""" 입풀력 """

'''
n = int(input())
a = list(map(int, input().split()))
n, m, k = map(int, input().split())
'''

# 입력을 빠르게 받아야 하는 경우
import sys
a = sys.stdin.readline().rstrip()
a = list(map(int, sys.stdin.readline().split()))\

# print()
a = 10
b = 20
print(a, b, sep=', ', end='\n')  # sep은 변수 사이 값 end는 입력후 값
print('a: ' + str(a))  # 자바에서는 문자열 변환 안해도 되지만 파이썬은 해야 됨
print('a:', a)  # 아니면 콤마로 구분
print(f'a: {a}')  # f-string 문법
print('a: {}'.format(a))  # format 사용
