array = []
for i in range(5):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

print("Array items:")
for i in range(len(array)):
    print(f"Element at index {i}: {array[i]}")

# Enter element 1: 2
# Enter element 2: 5
# Enter element 3: 7
# Enter element 4: 3
# Enter element 5: 9
# Array items:
# Element at index 0: 2
# Element at index 1: 5
# Element at index 2: 7
# Element at index 3: 3
# Element at index 4: 9
