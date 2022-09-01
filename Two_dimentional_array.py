row_num = int(input("input number of raw:"))
column_num = int(input("input number of column"))
two_dimensional_array =[[0 for col in range(column_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(column_num):
        two_dimensional_array[row][col] = row * col
        print(two_dimensional_array)

        print(type(two_dimensional_array))

#another example


from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
print(T[0])
print(T[1][2])


# 3rd example

T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
for r in T:
   for c in r:
      print(c,end = " ")
   print()


#We can insert new data elements at specific position by using the insert() method and specifying the index.
from array import *
T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

T.insert(2, [0, 5, 11, 13, 6])

for r in T:
    for c in r:
        print(c, end = " ")
        print()

