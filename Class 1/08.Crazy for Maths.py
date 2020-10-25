import math


def factorial(n):
    return 1 if n<=1 else n*factorial(n-1)


def estimate():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    contin_ue = True
    while contin_ue == True:
        numerator = float(factorial(4*k) * (1103 + 26390 * k))
        denominator = float(factorial(k)**4) * 396**(4*k)
        term = factor * float(numerator/denominator)
        total += term
        k += 1
        if term < 1e-15:
            contin_ue == False
            print ("Finished at iteration number", k)
            break
    return 1 / total

print(estimate())
