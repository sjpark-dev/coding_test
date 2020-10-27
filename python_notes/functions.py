""" 함수 """

# global 키워드
a = 0


def f():
    global a
    a += 1


f()
print(a)  # 1

# 람다 표현식 (Lambda Expression)
print((lambda x, y: x + y)(1, 1))  # 2
