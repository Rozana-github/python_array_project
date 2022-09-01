import array
arr = array.array('i', [10, 30, 41, 60, 17, 18])
print("the new created array is : " )
for i in range(0, 6):
    print(arr[i], end="")

# depending on index we can access the array

print("\r")

print(arr.index(10))
print(arr.index(30))
print(arr.index(41))
print(arr.index(60))
print(arr.index(18))
print(arr.index(17))
