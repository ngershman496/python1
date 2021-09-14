# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# This function collects user input to collect a name, number and a word
# No error checking is implemented so please use proper input
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   # print_hi("Nathan")
    get_info()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
