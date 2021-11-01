import sys

if __name__ == '__main__':
    vouels = ['a','A','e','E','i','I','o','O','u','U','y','Y']
    for i in range(len(sys.argv)):
        
        if i != 0:
            elem = sys.argv[i]
            if elem[0] in vouels:
                print(elem+'yay', end=' ')
            if elem[0] not in vouels and elem[1] not in vouels:
                sub = elem[:2]
                subelem = elem[2:] + sub + 'ay'
                print(subelem, end=' ')
            elif elem[0] not in vouels:
                sub = elem[:1]
                subelem = elem[1:] + sub + 'ay'
                print(subelem, end=' ')