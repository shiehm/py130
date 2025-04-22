file = open('example.txt', 'r')
print(repr(file.readline()))   # 'Running dog\n'
print(repr(file.readline()))   # 'Sleeping cat\n'
print(repr(file.readline()))   # 'Swimming fish\n'
print(repr(file.readline()))   # 'Singing bird\n'
print(repr(file.readline()))   # ''
print(repr(file.readline()))   # ''
file.close()

file = open('example.txt', 'r')
for line in file:
    print(repr(line))
# 'Running dog\n'
# 'Sleeping cat\n'
# 'Swimming fish\n'
# 'Singing bird\n'

file.close()

# Don't use a REPL to run this code
file = open('output.txt', 'w')
file.write('Hello, world!\n')
lines = ['First line\n', 'Second line\n']
file.writelines(lines)
file.close()

# Don't use a REPL to run this code
file = open('output.txt', 'a')
file.write('Third line!\n')
file.write('Last line!\n')
file.close()

file = open('output.txt', 'r')
for line in file:
    print(repr(line))
file.close()
