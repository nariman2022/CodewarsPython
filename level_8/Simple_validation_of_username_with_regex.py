# Write a simple regex to validate a username. Allowed characters are:
# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).

import re
def validate_usr(username):
    if 4 > len(username) < 16:
        return False
    x = re.findall('[a-z0-9_]', username)
    return len(x) == len(username)