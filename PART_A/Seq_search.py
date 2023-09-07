def sequential_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
array=[int(x) for x in input("Enter array:").split()]
target=int(input("Enter item"))
result=sequential_search(array,target)
if result !=-1:
    print("Element" ,target ,"found at",result)
else:
    print("Not available")

# Enter array:4 5 2 7 9 12
# Enter item9
# Element 9 found at 4
