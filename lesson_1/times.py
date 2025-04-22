def times(callback, count):
    for item in range(count):
        callback(item)


times(lambda number: print(number**2), 5)

pets = ('cat', 'dog', 'fish', 'bearded dragon')
new_pets = []
times(lambda index: new_pets.append(pets[index].title()), len(pets))
print(new_pets)