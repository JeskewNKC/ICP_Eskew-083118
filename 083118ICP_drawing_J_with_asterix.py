def size(n):
    '''Function takes n as number and prints a letter J out using * '''
    a = ("*")
    b = (" ")
    for i in range (1,n):
        if i == 1:
            print(a*n)
    for i in range(1,n):
        if i  < (n/2):
            print(' '*(2*n % 3)+' '+'*')
        elif i < (n-1):
            print(a + '  '+ a)
        else:
            print(a*3)
# n = int(input('Enter a number'))
size(7)

