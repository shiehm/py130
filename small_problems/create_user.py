"""
Create a function create_user that takes a username and requires 
keyword-only arguments for email and age.
"""

def create_user(username, *, email, age):
    return {
        'username': username,
        'email': email,
        'age': age
    }

print(create_user("Srdjan", email="srdjan@example.com", age=39))
# {"username": "Srdjan", "email": "srdjan@example.com", "age": 39}
try:
    print(create_user("Srdjan", "srdjan@example.com", age=39))
except TypeError as e:
    print(e)
# Raises an exception
