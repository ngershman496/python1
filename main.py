import os
import re
    
if __name__ == '__main__':

    current_user = os.getlogin()
    cores = os.cpu_count()
    print('Current user: ', current_user)
    print("Number of cores: ",cores)

    current_path = os.getcwd()
    match = re.search(current_user, current_path)

    with open('numbers.txt') as f:
        content = f.readlines()
    
    print('Using the expression \'\\d\\d\\d.\\d\\d.\\d\\d\\d\\d\'')
    for i in content:
        ssnMatch = re.search(r'\d\d\d\.\d\d\.\d\d\d\d', i)
        if ssnMatch :
            print('SSN Found! ', i)

    print('Using the expression \'[0-9]\{3\}\\.[0-9]\{2\}.[0-9]\{4\}\'')
    for i in content:
        ssnMatch = re.search(r'[0-9]{3}\.[0-9]{2}\.[0-9]{4}', i)
        if ssnMatch :
            print('SSN Found! ', i)

    if match:
        print(f'{current_user} was found in the path')
    else:
        print(f'{current_user} was not found in the path')