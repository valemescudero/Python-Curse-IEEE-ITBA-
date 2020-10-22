def num_pieces(max_num):
  pieces = max_num + 1
  for i in range(max_num):
    pieces += (i + 1)
  return pieces

def dom_pieces():
  max_num = int(input())
  pieces = num_pieces(max_num)
  print(pieces)

def max_value():
  max_num = 0
  x = int(input("Enter number of pieces\n"))
  pieces2 = 0

  while True:
    pieces2 = num_pieces(max_num)
    if pieces2 >= x:
      break
    if x != pieces2:
      max_num = max_num + 1

  if x == pieces2:
    print("Max num :", max_num)
  else:
    print("No game possible\n")
  sguir = int(input("presione 1 para continuar\n"))
  if sguir == 1:
    max_value()

max_value()
