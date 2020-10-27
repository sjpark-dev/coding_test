""" 사전 자료형 """

'''
Dictionary types are made up of key and value pair data.
They use hash table internally, 
which allows data search and update possible in O(1) time.
'''

# declare a dictionary
a = {}  # way 1
a = dict()  # way 2

# how to check if a key exists in a dictionary
a = dict()
a['name'] = 'John'  # {'name': 'John'} ('name' is the key, and 'John' is the value)
a['hobby'] = 'basketball'  # {'name': 'John', 'hobby': 'basketball'}
if 'age' in a:  # False because 'age' is not in dictionary a
    print('age key exists')

# dictionary functions
# .keys() returns keys
# .values() returns values
# .items() returns keys and values
