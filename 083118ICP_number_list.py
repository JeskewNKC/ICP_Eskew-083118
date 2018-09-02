"""Write a python program to take list of numbers as input and to return a tuple of first and
last numbers in the list."""
def get_list(n):
    y = []
    for i in n.split(","):
        y.append(i)
    # print (y)
    first_num = y[0]
    last_num = y[-1]
    first_num = int(first_num)
    last_num = int(last_num)
    z = (first_num, last_num)
    print (z)
n = input('Enter a list of numbers: ')
#print(n)
get_list(n)



