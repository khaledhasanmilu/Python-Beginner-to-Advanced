# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Adding an element
my_set.add(6)
print("After adding 6:", my_set)

# Removing an element
my_set.remove(3)
print("After removing 3:", my_set)

# Checking membership
print("Is 2 in the set?", 2 in my_set)

# Set operations
another_set = {4, 5, 6, 7, 8}
print("Another set:", another_set)

# Union
print("Union:", my_set | another_set)

# Intersection
print("Intersection:", my_set & another_set)

# Difference
print("Difference:", my_set - another_set)