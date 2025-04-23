"""
Write a function display_info that takes a positional-only 
parameter data, and keyword-only parameters reverse and uppercase.
"""
def display_info(string, /, *, uppercase=False, reverse=False):
    if uppercase:
        string = string.upper()
    if reverse:
        string = string[::-1]
    return string

print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC