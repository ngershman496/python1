import sys

def split1(str):
    for i in range(len(str)):
        if i != len(str)-1:
            if str[i] != ' ' and str[i+1] != ' ':
                print(str[i], end='')
            elif str[i] != ' ' and str[i+1] == ' ':
                print(str[i], end='\n')
        else:
            print(str[i])

def split2(str):
    splstr = str.split()
    for x in splstr:
        print(x)
    
if __name__ == '__main__':
    mystring = input("Enter a string: ")
    print('\nFunction 1:')
    split1(mystring)
    print('\nFunction 2:')
    split2(mystring)