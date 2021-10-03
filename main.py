# These imports are necessary for the random number generator
from random import randint, randrange
from random import seed

line_0 = '+-------+-------+-------+'
line_1 = '|       |       |       |'
line_2 = '|   1   |   2   |   3   |'
line_3 = '|   4   |   5   |   6   |'
line_4 = '|   7   |   8   |   9   |'
positions = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

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

#These are my fisrt version of Tic Tac Toe
# Use tic_tac_toe() in main to run
def print_board(pos, val):
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
    
    global positions
    pos -= 1
    if positions[pos] != ' ':
        return - 1
    else:
        positions[pos] = val
        line_0 = '+-------+-------+-------+'
        line_1 = '|       |       |       |'

        pos += 1
        spos = str(pos)
        
        global line_2
        global line_3
        global line_4

        if spos in line_2:
            line_2 = line_2.replace(spos, val)
        elif spos in line_3:
            line_3 = line_3.replace(spos, val)
        elif spos in line_4:
            line_4 = line_4.replace(spos, val)
        
        i = 1
        while i <= 13:
            if i == 1 or i == 5 or i == 9 or i == 13:
                print(line_0)
            elif i == 2 or i == 4 or i == 6 or i == 8 or i == 10 or i == 12:
                print(line_1)
            elif i == 3:
                print(line_2)
            elif i == 7:
                print(line_3)
            elif i == 11:
                print(line_4)
            i += 1

def get_user_selection():
    selection = int(input("Select your location: "))
    while print_board(selection, 'O') == -1:
        selection = int(input("Invalid input\n Please select again: "))
    return selection

def computer_move(num):
    seed = (num + 2) * num
    choice = 5
    while positions[choice-1] != ' ':
        choice = randint(1,9)
    return choice

def check_win():
    winner = ''
    if positions[0] == positions[1] and positions[0] == positions[2] and positions[0] != ' ' and positions[1] != ' ' and positions[2] != ' ': # top row
        winner = positions[0]
    elif positions[0] == positions[3] and positions[0] == positions[6] and positions[0] != ' ' and positions[3] != ' ' and positions[6] != ' ': # first col
        winner = positions[0]
    elif positions[3] == positions[4] and positions[3] == positions[5] and positions[3] != ' ' and positions[4] != ' ' and positions[5] != ' ': # second row
        winner = positions[3]
    elif positions[1] == positions[4] and positions[1] == positions[7] and positions[1] != ' ' and positions[4] != ' ' and positions[7] != ' ': # second col
        winner = positions[1]
    elif positions[6] == positions[7] and positions[6] == positions[8] and positions[6] != ' ' and positions[7] != ' ' and positions[8] != ' ': # third row
        winner = positions[6]
    elif positions[2] == positions[5] and positions[2] == positions[8] and positions[2] != ' ' and positions[5] != ' ' and positions[8] != ' ': # third col
        winner = positions[2]
    elif positions[0] == positions[4] and positions[0] == positions[8] and positions[0] != ' ' and positions[4] != ' ' and positions[8] != ' ': # left -> right
        winner = positions[0]
    elif positions[2] == positions[4] and positions[2] == positions[6] and positions[2] != ' ' and positions[4] != ' ' and positions[6] != ' ': # right -> left
        winner = positions[2]
    
    return winner

def tic_tac_toe():
    print_board(5,'X')
    s = 1
    turn = 1
    winner = check_win()
    #print(positions)
    while winner == '' and turn < 9:
        #print(positions)
        #print(turn)
        if turn % 2 == 1:
            selection = get_user_selection()
            print_board(selection, 'O')
            winner = check_win()
        if turn % 2 == 0:
            selection = computer_move(s)
            #print(selection)
            print_board(selection, 'X')
            winner = check_win()
            s += 5
        turn += 1
    if winner == 'O':
        print("You Win!")
    elif winner == 'X':
        print("Computer Wins")
    else:
        print("Tie Game")

#Used these for assignment 4
def display_board(board):
  
    line_0 = '+-------+-------+-------+'
    line_1 = '|       |       |       |'
    line_2 = f'|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |'
    line_3 = f'|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |'
    line_4 = f'|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |'



    i = 1
    while i <= 13:
        if i == 1 or i == 5 or i == 9 or i == 13:
            print(line_0)
        elif i == 2 or i == 4 or i == 6 or i == 8 or i == 10 or i == 12:
            print(line_1)
        elif i == 3:
            print(line_2)
        elif i == 7:
            print(line_3)
        elif i == 11:
            print(line_4)
        i += 1

def enter_move(board):
    move_list = make_list_of_free_fields(board)
    move = (1,1)

    while move not in move_list:
        choice = input("Enter your move: ")
        if choice == '1':
            move = (0,0)
        elif choice == '2':
            move = (0,1)
        elif choice == '3':
            move = (0,2)
        elif choice == '4':
            move = (1,0)
        elif choice == '5':
            move = (1,1)
        elif choice == '6':
            move = (1,2)
        elif choice == '7':
            move = (2,0)
        elif choice == '8':
            move = (2,1)
        elif choice == '9':
            move = (2,2)
    
    board[move[0]][move[1]] = 'O'

def make_list_of_free_fields(board):
    list = []

    out = 0
    for x in board:
        inner = 0
        for j in x:
            if j != 'X' and j != 'O':
                temp_tup = (out,inner)
                list.append(temp_tup)
            inner += 1
        out += 1
    return list

def victory_for(board, sign):
    winner = False
    if sign == 'X':
        player = 'Computer'
    else:
        player = 'You'

    #horizontal 
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        winner = True
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        winner = True    
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        winner = True
    
    #vertical
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        winner = True
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        winner = True
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        winner = True

    #diagonal
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        winner = True
    if board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        winner = True

    if winner and player == 'You':
        print(f'{player} Win!')
    elif winner and player == 'Computer':
        print(f'{player} Wins!')
    return winner

def draw_move(board):
    move_list = make_list_of_free_fields(board)
    if (1,1) in move_list:
        board[1][1] = 'X'
    else:
        num = len(move_list) 
        seed(num * num + 5)
        move = randint(0,num)

        move = move_list[move]
        board[move[0]][move[1]] = 'X'

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
    board = [['1','2','3'],
        ['4','5','6'],
        ['7','8','9']]
    turn = 0
    done = False
    winner = ''
    while turn < 9 and not done:
        draw_move(board)
        turn += 1
        display_board(board)
        done = victory_for(board, 'X')
        if done:
            winner = 'X'
            break
        if turn == 9:
            break
        enter_move(board)
        turn += 1
        display_board(board)
        done = victory_for(board, 'O')
        if done:
            winner = 'O'
            break
        
    if winner == '':
        print('No Winner. Tie Game!')

# if the file name is __main__ than run these methods
if __name__ == '__main__':
# Uncomment to view results of each assignment 
#    assignment_1()
#    assignment_2()
#    assignment_3()
    assignment_4()
        