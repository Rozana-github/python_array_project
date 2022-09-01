'''
-Create a one_dimensional integer array
and insert numbers to the maximum size provided until the end of the array.
-Acess the number inserted and then display the same as output.
'''

'''
Here, we declare an empty array. 
Python for loop and range() function is used to initialize an array with a default value. 
You might get confused between lists and arrays but lists are dynamic arrays.
Also, arrays stores similar type of data in it while lists store different types of data.
'''


print("How many elements are to store inside the array:-")
num = int(input())
print("Enter", num, "Element :\n")

arr = []    # define array with empty list
for i in range(num):
    element = input()
    arr.append(element)
    print(" \n the array list element are :")

for i in range(num):
    print(i, arr[i])
print(type(arr))

'''Creating Array
using array Module'''


from array import *
array1 = array('i', [10, 20, 30, 40, 50])
for x in array1:

    print(x)

    print(type(array1))



