# Task:
# Write a function that will accept two parameters: variable and type and check if type of variable is matching type. Return true if types match or false if not.

def type_validation(variable, _type):
    return _type in str (type(variable))