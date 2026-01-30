# In honor of my grandfather's memory we will write a function using his formula!
#
# Take a list of ages when each of your great-grandparent died.
# Multiply each number by itself.
# Add them all together.
# Take the square root of the result.
# Divide by two.

def predict_age(*age):
    return int((sum([c ** 2 for c in (age)]) ** 0.5) / 2)