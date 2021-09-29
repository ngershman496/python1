# These imports are necessary for the random number generator
from random import randint
from random import seed

# used for assignment_1
def print_hi(name):
    print(f'Hi, {name}')

# used for assignment_2
def get_info():
    name = input("Enter your name: ")
    print(f'Hello, {name}')
    x = int(input('Enter a number: '))  # this will cast the input to an int so math can be preformed
    print(x, "*", x, "is", x ** 2)
    word = input("Enter a word: ")
    print(f'The length of \'{word}\' is {word.__len__()}')

# used for assignment_3
def print_art():
    #   |                   |
    #   |                   |
    #   |                   |
    #   |        <^>        |
    #   ||===I||(-@-)||I===||
    #   |        \_/        |
    #   |                   |
    #   |                   |
    #   |                   |
    #   |                   |
    #   |                   |\


    art =[[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            ['|','|','|','|','|','|','|','|','|','|','|'],
            [' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','=',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','=',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','=',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','(',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','<','-','\\',' ',' ',' ',' ',' '],
            [' ',' ',' ','^','@','_',' ',' ',' ',' ',' '],
            [' ',' ',' ','>','-','/',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',')',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','=',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','=',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ','=',' ',' ',' ',' ',' ',' '],
            ['|','|','|','|','|','|','|','|','|','|','|']]

    x = len(art)
    y = len(art[0])

    for i in range(len(art[0])):
        for j in range(len(art)):
            print(art[j][i], end='')
        print()

def flip_coin(i):


    choice = 2
    while choice != 1 and choice != 0:
        choice = int(input("Select '0' or '1': "))
        if choice != 1 and choice != 0:
            print("Invalid choice")
    seed((i+5)*i)
    flip = randint(0,1)

    print("The coin is " , flip)
    
    if flip == int(choice):
        print("You win!")
    else:
        print("You lost :(")

# LINES 85 - 114 WORK IN PROGRESS
# used for assignment_4
def print_board(pos: int, val: str):
    # +-------+-------+-------+
    # |       |       |       |
    # |   1   |   2   |   3   |
    # |       |       |       |
    # +-------+-------+-------+
    # |       |       |       |
    # |   4   |   5   |   6   |
    # |       |       |       |
    # +-------+-------+-------+
    # |       |       |       |
    # |   7   |   8   |   9   |
    # |       |       |       |
    # +-------+-------+-------+
    positions = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    if positions[pos] != ' ':
        return -1
    else:
        positions[pos] = str

def get_user_selection():
    selection = int(input("Select your location: "))
    while print_board(selection, 'O') == -1:
        selection = int(input("Invalid input\n Please select again: "))

def tic_tac_toe():
    print_board(5,'X')
    selection = get_user_selection()
    print_board(selection, 'O')
        

# these are used to only have function calls in the main script
def assignment_1():
    print_hi('Nathan Gershman')

def assignment_2():
    get_info()

def assignment_3():
    resp = 1
    counter = 1
    while resp == 1:
        choice = 0
        while choice != 1 and choice != 2:
            choice = int(input("Would you like to print art(1) or flip a coin(2): "))
            if choice != 1 and choice != 2:
                print("Invalid imput\nPlease chose 1 or 2")
        if choice == 1:
            print_art()
        elif choice == 2:
            flip_coin(counter)
        
        resp = input("Enter 1 to go again: ")
        if resp == '1':
            resp = 1
        else:
            resp = 0
        counter+=1

def assignment_4():
    print()

# if the file name is __main__ than run these methods
if __name__ == '__main__':
# Uncomment to view results of each assignment 
#    assignment_1()
#    assignment_2()
#    assignment_3()
    print()