import array

# Create an array of integers
numbers = array.array('i', [10, 20, 30, 40, 50])

# Print all elements
print("Array elements:")
for num in numbers:
    print(num)

# Append a new element
numbers.append(60)
print("\nAfter appending 60:", numbers.tolist())

# Insert an element at index 2
numbers.insert(2, 25)
print("After inserting 25 at index 2:", numbers.tolist())

# Remove an element
numbers.remove(30)
print("After removing 30:", numbers.tolist())

# Access by index
print("Element at index 3:", numbers[3])
