import numpy as np

def inner_pattern(n):
    size = n+(n-1)
    front = 0
    back = size - 1
    lst =  np.zeros(shape = (size, size))
    lst = np.asmatrix(lst)
    while n != 0:
        for i in range(front,back+1):
            for j in range(front,back+1):
                if i == front or i == back or j == front or j == back:
                    lst[i,j] = n
        n -=1
        front +=1
        back -=1
    print (str(lst).replace(' ','').replace('.',' ').replace('[','').replace(']',''))

inner_pattern(5)