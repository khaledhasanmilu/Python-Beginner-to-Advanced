# Set methods
print("\nSet Methods:")

# Clear the set
my_set.clear()
print("After clearing:", my_set)

# Create a new set
my_set = {1, 2, 3, 4, 5}

# Copy the set
copied_set = my_set.copy()
print("Copied set:", copied_set)

# Discard an element (no error if not present)
my_set.discard(3)
print("After discarding 3:", my_set)

# Pop an element (removes and returns an arbitrary element)
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("Set after popping:", my_set)

# Update the set with elements from another set
my_set.update({6, 7, 8})
print("After updating:", my_set)
