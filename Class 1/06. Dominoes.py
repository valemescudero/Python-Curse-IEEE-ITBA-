def num_pieces(max_num):
  pieces = max_num + 1
  for i in range(max_num):
    pieces += (i + 1)
  return pieces

def get_num_pieces():
  max_num = int(input("Please, enter the highest number in the set:\n"))
  pieces = num_pieces(max_num)
  print("The number of pieces is:", pieces)
  cont = int(input("\nEnter 1 to try again or 2 to go back\n"))
  if cont == 1:
    get_num_pieces()

def set():
  max_num = int(input("Please, enter the highest number in the set:\n"))
  x = 0
  for i in range(max_num+1):
    for j in range(x,max_num+1):
      print(i, "-", j)
    x = x+1
  cont = int(input("\nEnter 1 to try again or 2 to go back\n"))
  if cont == 1:
    set()

def max_value():
  max_num = 0
  x = int(input("Please, enter number of pieces in the set:\n"))
  pieces = 0

  while True:
    pieces = num_pieces(max_num)
    if pieces >= x:
      break
    if x != pieces:
      max_num = max_num + 1

  if x == pieces:
    print("The highest number in the set is:", max_num)
  else:
    print("No game possible\n")
  cont = int(input("\nEnter 1 to try again or 2 to go back\n"))
  if cont == 1:
    max_value()

def menu():
  print("Welcome.")
  while True:
    print("\nEnter:")
    print("1 to find the number of pieces for a highest number")
    print("2 to see the set for a highest number")
    print("3 to find the highest number if a set is possible with the given amount of pieces")
    print("or 4 to exit\n")
    option = int(input())
    print("")

    if option == 1:
      get_num_pieces()
    elif option == 2:
      set()
    elif option == 3:
      max_value()
    else:
      print("Goodbye!")
      break


menu()
