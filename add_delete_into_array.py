# sort element of an array

# what is the size of an array ?
print("Enter the size of an array:")
tot = int(input())
print("enter " + str(tot) + "element")

# create an array depend on the size of the array and insert data by giving input from keyboard
arr = []
for i in range(tot):
    arr.append(input())
    print(i, arr[i])


# to delete element from the array

print("enter the value to delete")
val = input()
if val in arr:
    arr.remove(val)
    print("the new array is :")

    for i in range(tot - 1):
        print(i, arr[i])
else:
    print("\n the element does not exist in the list")







