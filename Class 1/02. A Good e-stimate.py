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
  places = int(input("Please, enter number of decimal places from Euler's number you wish to print:\n"))
  print("Euler's number:",f"%.{places}f" % e_num)

e_num = taylor(80)
e_num = truncate_f(e_num)
