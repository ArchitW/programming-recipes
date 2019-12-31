'''
finds unique elements in list.
converts list in set, be careful
'''

array = [1,1,1,1,2,3,4,4,44,5,55,5,5,5,5,6,6,66,6]

' gives set'
method1 = (set(array))
method2 = {i for i in array}
method3 = {*array}
'to convert it to list use(list())'
print(list(set(array)))