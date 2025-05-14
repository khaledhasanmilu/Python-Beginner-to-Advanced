# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Initial List:", fruits)

# Accessing elements by index
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])  # Negative index

# Adding items
fruits.append("mango")
print("After append:", fruits)

fruits.insert(1, "orange")  # Insert at index 1
print("After insert:", fruits)

# Removing items
fruits.remove("banana")  # Removes first occurrence
print("After remove:", fruits)

popped = fruits.pop()  # Removes and returns the last item
print("After pop:", fruits)
print("Popped item:", popped)

# Replacing items
fruits[0] = "grape"
print("After replacement:", fruits)

# Length of list
print("Length of list:", len(fruits))

# Looping through list
print("Loop through list:")
for fruit in fruits:
    print("-", fruit)

# Check if an item exists
if "cherry" in fruits:
    print("Cherry is in the list!")

# Sorting
fruits.sort()
print("Sorted list:", fruits)

# Reversing
fruits.reverse()
print("Reversed list:", fruits)

# Copying list
new_list = fruits.copy()
print("Copied list:", new_list)

# Clear all items
fruits.clear()
print("After clearing:", fruits)
