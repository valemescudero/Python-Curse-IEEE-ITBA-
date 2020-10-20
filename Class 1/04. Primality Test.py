#  Write a function that recieves a number and returns True when it's a prime number and False when it's not.
#  Through a for loop check for the primality of numbers 1 to 20.


def is_prime(num):
  if num == 1:
    primality = False
  else:
    primality = True
  
  if num > 2:
    rang = (num ** 0.5)
    rang = int(rang)
    for i in range(rang):
      if num % (i + 2) == 0:
        print(num, "is divisible by", i + 2)
        primality = False;
        break
  return primality

for i in range(20):
  num = i + 1
  primality = is_prime(num)
  if primality == True:
    print(num, "is a prime number.")
  else:
    print(num, "is not a prime number.")
