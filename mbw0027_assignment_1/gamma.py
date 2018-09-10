import math

def gamma(n=0):
    return function(n/2)

def function(n = 0):
    if (n == None):
        return 0
    if (n == 1.0):
        return 1
    if (n == 1.0/2.0):
        return math.sqrt(math.pi)
    return ((n-1) * function(n-1))

print gamma(5.0)