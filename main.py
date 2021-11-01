import sys

def help():
    print("This is how you use this program")
    print('-h  help option, displays help page')
    print('-L  the next string of numbers will be converted to LED light symbols\n\tEx: main.py -L 33')
    print('-A  add the next two numbers, must be int value\n\tEx: main.py -A 20 55')
    
def lights(num):

    lightarr1 = [[' ',' ','#'],
                [' ',' ','#'],
                [' ',' ','#'],
                [' ',' ','#'],
                [' ',' ','#']]

    lightarr2 = [['#','#','#'],
                [' ',' ','#'],
                ['#','#','#'],
                ['#',' ',' '],
                ['#','#','#']]

    lightarr3 = [['#','#','#'],
                [' ',' ','#'],
                ['#','#','#'],
                [' ',' ','#'],
                ['#','#','#']]

    lightarr4 = [['#',' ','#'],
                ['#',' ','#'],
                ['#','#','#'],
                [' ',' ','#'],
                [' ',' ','#']]

    lightarr5 = [['#','#','#'],
                ['#',' ',' '],
                ['#','#','#'],
                [' ',' ','#'],
                ['#','#','#']]

    lightarr6 = [['#','#','#'],
                ['#',' ',' '],
                ['#','#','#'],
                ['#',' ','#'],
                ['#','#','#']]

    lightarr7 = [['#','#','#'],
                [' ',' ','#'],
                [' ',' ','#'],
                [' ',' ','#'],
                [' ',' ','#']]

    lightarr8 = [['#','#','#'],
                ['#',' ','#'],
                ['#','#','#'],
                ['#',' ','#'],
                ['#','#','#']]

    lightarr9 = [['#','#','#'],
                ['#',' ','#'],
                ['#','#','#'],
                [' ',' ','#'],
                [' ',' ','#']]

    lightarr0 = [['#','#','#'],
                ['#',' ','#'],
                ['#',' ','#'],
                ['#',' ','#'],
                ['#','#','#']]

    for r in range(5):
        for ix in range(len(num)):
            for c in range(3):
                if num[ix] == '1':
                    print(lightarr1[r][c], end='')
                if num[ix] == '2':
                    print(lightarr2[r][c], end='')
                if num[ix] == '3':
                    print(lightarr3[r][c], end='')
                if num[ix] == '4':
                    print(lightarr4[r][c], end='')
                if num[ix] == '5':
                    print(lightarr5[r][c], end='')
                if num[ix] == '6':
                    print(lightarr6[r][c], end='')
                if num[ix] == '7':
                    print(lightarr7[r][c], end='')
                if num[ix] == '8':
                    print(lightarr8[r][c], end='')
                if num[ix] == '9':
                    print(lightarr9[r][c], end='')
                if num[ix] == '0':
                    print(lightarr0[r][c], end='')
            print(' ', end='')
        print()

def add(num1, num2):
    add1 = int(num1)
    add2 = int(num2)

    return add1+add2

if __name__ == '__main__':
    flag_found = False
    try:
        for i in range(len(sys.argv)-1):
            if len(sys.argv) == 2 and sys.argv[1] == '-h':
                help()
                flag_found = True
            if len(sys.argv) > 2 and sys.argv[i] == '-h':
                raise Exception('-h Option cannot be used with other parameters')
            if sys.argv[i] == '-L':
                lights(sys.argv[i+1])
                flag_found = True
            if sys.argv[i] == '-A':
                print(add(sys.argv[i+1], sys.argv[i+2]))
                flag_found = True
        if not flag_found:
            print('Improper use.\nUse -h for help')
    except:
        print('Invalid use\nUse -h option to view help.')