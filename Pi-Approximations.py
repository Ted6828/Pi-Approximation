from random import random
import time

def piCalc(recur):
    pi, den, operator = 3, 2, 1
    for i in range(0, recur):
        pi = (pi) + (operator * 4 / ((den) * (den + 1) * (den + 2)))
        if operator == 1:
            operator = -1
        else:
            operator = +1
        den = den + 2
    return pi

def piCalc2(total):
    count = 0
    for i in range(total):
        x = random()
        y = random()
        if x*x + y*y <= 1:
            count = count + 1
    return str(4 * count / total)

def piCalc3(recur):
    pi, den, operator = 0, 1, 1
    for i in range(0, recur):
        pi = (pi) + (operator * 4 / (den))
        if operator == 1:
            operator = -1
        else:
            operator = +1
        den = den + 2
    return pi

precision = int(input("Enter precision... : "))
print("")
start = time.time()
print("Pi using Nilakantha Series:", piCalc(precision))
end1 = time.time()
print("Pi using Gregory-Leibniz Series:", piCalc3(precision))
end2 = time.time()
print("Pi using Monte Carlo Method:", piCalc2(precision))
end3 = time.time()
print("")
print("Time taken by Nilakantha Series:", end1 - start , "seconds")
print("Time taken by Gregory-Leibniz Series:", end2 - end1 , "seconds")
print("Time taken by Monte Carlo Method:", end3 - end2 , "seconds")
