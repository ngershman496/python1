from Bird import Bird 

def get_name():
    return input('What is the name of this bird? ')

if __name__ == '__main__':
    
    name1 = get_name()
    bird1 = Bird(name1)
    print()
    name2 = get_name()
    bird2 = Bird(name2)

    print()
    bird1.introduction()
    print()
    bird2.introduction()
    
    