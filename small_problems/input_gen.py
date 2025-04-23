"""
Create a generator function that yields user input strings until the word "stop" is entered.
"""

def user_input_generator():
    while True:
        user_input = input('Write something. Write "stop" to stop. ')
        if user_input == 'stop':
            break
        yield user_input

print(list(user_input_generator()))