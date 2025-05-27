import os

filename = "sample.txt"

# 1. Write to a file (creates file if not exists, overwrites if exists)
with open(filename, "w") as file:
    file.write("Hello, this is a file handling example in Python.\n")
    file.write("This line is written using the write() function.\n")

# 2. Read from the file
print("Reading the file content:")
with open(filename, "r") as file:
    content = file.read()
    print(content)

# 3. Append to the file
with open(filename, "a") as file:
    file.write("This line is added later using append mode.\n")

# 4. Read again to see the appended content
print("\nReading the updated file content:")
with open(filename, "r") as file:
    updated_content = file.read()
    print(updated_content)

# 5. Optional: Check if file exists before reading
if os.path.exists(filename):
    print("\nFile exists and ready to use.")
else:
    print("\nFile not found.")
