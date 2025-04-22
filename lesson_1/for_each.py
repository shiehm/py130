def for_each(callback, iterable):
    for element in iterable:
        callback(element)
        
for_each(lambda string: print(string.upper()), ['hi', 'my', 'name', 'is'])
for_each(lambda num: print(num*2), [1, 2, 3, 4, 5])

nested_list = [[1, 2], [3, 4]]
for_each(lambda sublist: sublist.pop(), nested_list)
print(nested_list)