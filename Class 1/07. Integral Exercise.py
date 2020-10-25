def f(x):
    return x**2 + 2

def integral(f, a, b, dx):
    n = 0
    area = 0
    while a + n * dx <= b:
        area_segment = f(a + n * dx) * dx
        n += 1
        area += area_segment
    return area

print("Welcome!")
a = float(input("Please, enter starting point:\n"))
b = float(input("Enter ending point:\n"))
dx = float(input("Enter segment value:\n"))

print("The area below the curve is: ", integral(f, a, b, dx))
