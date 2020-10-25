""" 집합 자료형 """

# declare empty set
a = set()

# initialize a set
a = set([1, 2, 2, 3]) # way 1
a = {1, 2, 2, 3} # way 2

# set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5} (합집합)
print(a & b)  # {3} (교집합)
print(a - b)  # {1, 2} (차집합)

'''
set functions
.add() adds element to set, O(1) 
.update() adds multiple elements to set
    ex) a.update([5, 6])
.remove(element) removes an element from set, O(1)
'''
