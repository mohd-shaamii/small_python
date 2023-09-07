def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
array = [int(x) for x in input("Enter the elemnts:").split()]
bubble_sort(array)
print("Sorted array:",array)

# Enter the elemnts:12 54 32 89 23
# Sorted array: [12, 23, 32, 54, 89]
