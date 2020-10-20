#  Print n numbers from the Fibonacci sequence


a, b = 0, 1
print("How many numbers would you like to display?")
num = int(input())

print("\n")
print(a)
print(b)
for i in range(num - 1):
  c = a + b
  print(c)
  a, b = b, c
