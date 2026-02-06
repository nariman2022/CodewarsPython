# Two red beads are placed between every two blue beads. There are N blue beads.
# Implement a function returning the number of red beads.
def count_red_beads(n):
    return (n-1) * 2 if n > 2 else 0