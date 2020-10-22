#  Although traditional dominoes is played with tiles featuring combinations of spot counts between zero and six,
#  we are going to play with the idea of a maximum number n of spots

#  Write a function to calculate the tiles necessary for a complete set with the maximum number of spots n from input
#  Bear in mind, every combination of two numbers should happen only once

#  Write a second function to print every posible combination for a complete set with the maximum number of spots n from input

#  Additional 3 Stars Challenge:
#  Write a function to calculate, for an input given amount of tiles, the value of n (the maximum number of spots) when a game set is possible
#  considering that when none is possible, it should print "No game possible".


def num_tiles(max_num):
    tiles = max_num + 1
    for i in range(max_num):
        tiles += (i + 1)
    return tiles


def get_num_tiles():
    max_num = int(input("Please, enter the maximum number in the set:\n"))
    tiles = num_pieces(max_num)
    print("The number of tiles is:", tiles)
    cont = int(input("\nEnter 1 to try again or 2 to go back\n"))
    if cont == 1:
        get_num_tiles()

    
def domino_set():
    max_num = int(input("Please, enter the maximum number in the set:\n"))
    repetition_avoider = 0
    for i in range(max_num+1):
        for j in range(repetition_avoider,max_num+1):
            print(i, "-", j)
        repetition_avoider = repetition_avoider+1
    cont = int(input("\nEnter 1 to try again or 2 to go back\n"))
    if cont == 1:
        domino_set()

    
def max_value():
    max_num = 0
    tiles = int(input("Please, enter number of tiles in the set:\n"))
    aux_tiles = 0
    while True:
        aux_tiles = num_pieces(max_num)
        if aux_tiles >= tiles:
            break
        if tiles != aux_tiles:
            max_num = max_num + 1
    if tiles == aux_tiles:
        print("The maximum number in the set is:", max_num)
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
        print("4 to exit\n")
        option = int(input())
        print("")

        if option == 1:
            get_num_tiles()
        elif option == 2:
            domino_set()
        elif option == 3:
            max_value()
        else:
            print("Goodbye!")
            break

      
menu()
