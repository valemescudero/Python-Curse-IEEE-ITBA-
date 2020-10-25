#  Collatz's conjecture 
#  Write a program to receive an input number and have it work with the following pattern using a while loop:

#  when the number is even, have it divided by two
#  and when it's odd, have it multiplied by three and add one to the result

#  This process should stop at one and print the number of steps it took to get there
#  Example, for n == 6 the sequence would be 6,3,10,5,16,8,4,2,1 and the number of steps, 8.


def collatz():
    n = int(input("Please, enter a number to begin:\n"))
    steps = 0
    print("\nThe process:")
    print(n)
    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(n * 3 + 1)
        print(n)
        steps = steps + 1
    print("\nSteps needed:", steps)


collatz()
