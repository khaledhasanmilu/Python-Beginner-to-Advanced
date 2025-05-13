# Define a sample string
s = "  Hello World!  "
print("Original string:", repr(s))

# Length of string
print("Length:", len(s))

# Convert to lowercase
print("Lowercase:", s.lower())

# Convert to uppercase
print("Uppercase:", s.upper())

# Remove leading and trailing whitespaces
print("Strip:", s.strip())

# Remove only leading whitespaces
print("Lstrip:", s.lstrip())

# Remove only trailing whitespaces
print("Rstrip:", s.rstrip())

# Replace substring
print("Replace 'World' with 'Python':", s.replace("World", "Python"))

# Find substring
print("Find 'World':", s.find("World"))  # returns -1 if not found

# Index of substring (raises error if not found)
try:
    print("Index of 'World':", s.index("World"))
except ValueError:
    print("Index: 'World' not found")

# Count occurrences
print("Count of 'l':", s.count("l"))

# Join list of strings
words = ["Python", "is", "fun"]
print("Join:", " ".join(words))

# Split string
print("Split:", s.strip().split())  # removes extra space before splitting

# Startswith and endswith
print("Starts with '  He':", s.startswith("  He"))
print("Ends with '!  ':", s.endswith("!  "))

# isalpha (checks if all are letters)
print("Is alpha:", s.isalpha())

# isdigit (checks if all are digits)
print("Is digit:", s.isdigit())

# isalnum (checks if all are letters or digits)
print("Is alnum:", s.isalnum())

# Swap case (lower to upper and vice versa)
print("Swap case:", s.swapcase())

# Title case
print("Title case:", s.title())

# Capitalize
print("Capitalize:", s.capitalize())

# Reverse string
print("Reversed:", s[::-1])

# f-string formatting
name = "Khalid"
age = 22
print(f"Formatted string (f-string): Name: {name}, Age: {age}")

# format() method
print("Formatted string (format): Name: {}, Age: {}".format(name, age))
