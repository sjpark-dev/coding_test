""" 조건문 """

'''
기타 연산자
in, not in 연산자는 리스트, 튜플, 문자열, 사전 자료형 등
여러개의 데이터를 담는 자료형에 사용할 수 있다.
'''

# pass keyword
if 5 > 2:
    pass

# 조건부 표현식 (Conditional Expression) if ~ else
n = 10
res = 1 if n >= 5 else 0  # 1

print(1) if 5 > 2 else print(2)  # 1

# 0 < x < 10 is possible in python but probably not in other languages
x = 5
if 0 < x < 10:  # True
    print(1)
if 0 < x and x < 10:  # Same code as above
    print(1)
