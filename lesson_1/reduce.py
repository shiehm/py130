def reduce(callback, iterable, start):
    accumulator = start
    for item in iterable:
        accumulator = callback(item, accumulator)
    return accumulator

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))     # 300

numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
print(reduce(total, numbers, 0))        # 31

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))      # 300

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ''))      # ROYGBIV

numbers = [3, 7, 2, 9, 5]
sum_sq = lambda num, accum: accum + num**2
print(reduce(sum_sq, numbers, 0))