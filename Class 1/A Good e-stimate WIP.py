def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac = fac * i
    return fac


def taylor(n):
    e = 1
    for i in range(1, n+1):
        e = e + 1 / factorial(i)
    return e


def truncate_f(e_num):
    places = int(input("Please, enter number of decimal places from e you desire to print:\n"))
    i = e_num.index(".")
    truncated = e_num[:i + places]
    truncated = float(truncated)
    return truncated

e_num = str(taylor(80))
e_num = truncate_f(e_num)

    
print("Euler's number:", e_num)
