from random import random

def piCalc(recur):
    pi, den, operator = 3, 2, 1
    for i in range(0, recur):
        pi = (pi) + (operator * 4 / ((den) * (den + 1) * (den + 2)))
        if operator == 1:
            operator = -1
        else:
            operator = +1
        den = den + 2
    return(pi)

def piCalc2(total):
    count = 0
    for i in range(total):
        x = random()
        y = random()
        if x*x + y*y <= 1:
            count = count + 1
    return str(4 * count / total)

print("Pi using Nilakantha Series:", piCalc(500000))
print("Pi using Monte Carlo Method:", piCalc2(500000))