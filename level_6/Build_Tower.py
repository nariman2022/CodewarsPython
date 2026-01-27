Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
A tower block is represented with "*" character.
For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ",
  "*****"
]

def tower_builder(n_floors):
    tower = []
    for n in range(n_floors):
        space = ' ' * (n_floors - n - 1)
        star = '*' * (2 * n + 1)
        tower.append(space + star + space)
    return tower