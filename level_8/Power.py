#The goal is to create a function of two inputs number and power, that "raises" the number up to power (ie multiplies number by itself power times).

def number_to_pwr(number, p):
    summ = 1
    for i in range(p):
        summ *= number
    return summ