maxNum = int(input())

fichas = maxNum + 1
for i in range(maxNum):
  fichas += (i + 1)

print(fichas)

def game():
  max_num = int(input())
  x = 0
  for i in range(max_num+1):
    for j in range(x,max_num+1):
      print(i, "-", j)
    x = x+1
game()
