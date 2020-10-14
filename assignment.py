#! python3

import math

def tempConversion(C,unit):
    if unit=="F":
        return float(round((C-32)*5/9))
    else:
        return float(round((C*9/5)+32))

def factorPair(x,y):
    lis=[int(y)]
    lis.append(int(x/y))
    lis.sort()
    return lis

def cosineLaw(A,B,C,oppositeSide=True):
    if oppositeSide == False:
       return solution(quadratic(1,B,C))
    else:
        c = math.sqrt((A**2)+(B**2)-(2*A*B*math.cos(toRadians(C))))
        return c
          
def toRadians(x):
    return ((x*math.pi)/180)

def solution(n):
    if n[0] > 0:
        return n[0]
    else:
        return n[1]

def quadratic(a,b,c):
    x1 = (-1*b + math.sqrt(b**2 - 4 * a*c)) / (2*a)
    x2 = (-1*b - math.sqrt(b**2 - 4 * a*c)) / (2*a)
    z = [x1,x2]
    z.sort()
    return(z)