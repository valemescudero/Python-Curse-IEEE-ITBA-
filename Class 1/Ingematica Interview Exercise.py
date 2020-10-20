#  Write a program to print numbers 1 to 100 and:
#  N3 when it's a multiple of 3
#  N5 for multiples of 5
#  and N3N5 for multiples of both 3 and 5


def printNums():
  for i in range(100):
    print(i + 1)
    if (i+1) % 3 == 0 and (i+1) % 5 == 0:
      print("N3N5")
    elif (i+1) % 3 == 0:
      print("N3")
    elif (i+1) % 5 == 0:
      print("N5")
  print("\n")


printNums()
