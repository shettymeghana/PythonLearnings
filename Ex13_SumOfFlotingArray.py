'''
Write a function named "subtotal" takes as its arguments the following:
(1) an array of floating point values;(2) an integer that tells the number of cells in the array.
The function should replace the contents of each cell with the sum of the contents of all the cells in the original array from
the left end to the cell in question. Thus, for example, if the array passed to the function looks like this:
0    1     2     3     4
5.8 | 2.6 | 9.1 | 3.4 | 7.0
then when the function returns, the array will have been changed so that it looks like this:
0    1     2      3      4
5.8 | 8.4 | 17.5 | 20.9 | 27.9
Because 5.8 + 2.6 = 8.4 and 5.8 + 2.6 + 9.1 = 17.5 and so on. Note that the contents of cell 0 are not changed.
The function should not return a value.
'''
import numpy as np
def subTotal(arr):
    new_arr = []
    for index,value in enumerate(arr):
        if index == 0:
            new_arr.append(arr[index])
        else:
            new_arr.append(arr[index] + new_arr[index - 1])
    #print new_arr
    abc = [round(elem, 2) for elem in new_arr]
    print abc

if __name__ == '__main__':

    print "(1) an array of floating point values \n+++++++++++++***************++++++++++++"
    print "Enter values to the array"
    a = [float(x) for x in raw_input().split()]
    subTotal(a)

    a = []
    new_a = []
    print "\n(2) an integer that tells the number of cells in the array \n+++++++++++++***************++++++++++++"
    print"Enter size of list"
    sizeofList = raw_input('---> ')
    print "Enter values to the array"
    for i in range(0, int(sizeofList)):
        a.append(raw_input('---> '))
    for item in a:
        new_a.append(float(item))
    subTotal(new_a)




