# Pi Approximator 

These are three simple functions written in python which uses the Nilakantha Series ( which was developed in the 15th century. ),Monte Carlo method and the Gregory-Leibniz series.

## How it works

The Nilakantha Series is the formula below it  works out an approximation of pi depending on the amount of times it recurs on for using the equation below.

![alt text](https://www.mathscareers.org.uk/wp-content/ql-cache/quicklatex.com-a3dba30db136def060827e83c2837443_l3.svg)

The Gregory-Leibniz Series is very similar to the Nilakantha Series with just using a different equation 
![alt text](https://i.stack.imgur.com/sRrzJ.png)


However the Monte Carlo method involves creating a square with an inner circle of the same dimensions and plotting random points. Then dividing the points in the circle by the total points and multiplying by 4.
![alt text](https://images.squarespace-cdn.com/content/v1/54e50c15e4b058fc6806d068/1425423073377-E2QATXP5SYN4RUZJ82D2/image-asset.png?format=200w)

## The Functions

Nilakantha Series
```python
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
```
Monte Carlo methord
```python
def piCalc2(total):
    count = 0
    for i in range(total):
        x = random()
        y = random()
        if x*x + y*y <= 1:
            count = count + 1
    return str(4 * count / total)
```
Gregory-Leibniz series
```python
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
```

## Usage

Simply call the functions with a specified amount to recur, higher the amount higher the precision.
For the Monte Carlo methord you need to import random but the others dont require anything
```python
print("Pi using Nilakantha Series:", piCalc(500000))
```
```python
print("Pi using Monte Carlo Method:", piCalc2(500000))
```
```python
print("Pi using Gregory-Leibniz series:", piCalc3(500000))
```

## Warning
I might of got some of the terminology wrong so dont quote me on anything.