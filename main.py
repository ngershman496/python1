from random import randint
from random import seed

def get_info():
    name = input("Enter your name: ")
    print(f'Hello, {name}')
    x = int(input('Enter a number: '))  # this will cast the input to an int so math can be preformed
    print(x, "*", x, "is", x ** 2)
    word = input("Enter a word: ")
    print(f'The length of \'{word}\' is {word.__len__()}')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

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

if __name__ == '__main__':
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
