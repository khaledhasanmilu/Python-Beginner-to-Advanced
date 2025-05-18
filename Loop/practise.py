# Python Loops - All-in-One Example

# FOR LOOP with list
fruits = ["apple", "banana", "cherry"]
print("For loop with list:")
for fruit in fruits:
    print(fruit)

# FOR LOOP with range
print("\nFor loop with range:")
for i in range(5):
    print(i)

# FOR LOOP with range(start, stop, step)
print("\nFor loop with range(start, stop, step):")
for i in range(1, 10, 2):
    print(i)

# WHILE LOOP
print("\nWhile loop:")
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# BREAK in loop
print("\nBreak in for loop:")
for i in range(10):
    if i == 4:
        break
    print(i)

# CONTINUE in loop
print("\nContinue in for loop:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# PASS in loop
print("\nPass in for loop (does nothing):")
for i in range(3):
    pass  # Placeholder

# NESTED LOOPS
print("\nNested loops:")
for i in range(2):
    for j in range(2):
        print(f"i={i}, j={j}")

# LOOP with ELSE
print("\nFor loop with else:")
for i in range(3):
    print(i)
else:
    print("Loop finished without break")

# Real-world example: Sum of first 10 numbers
print("\nSum of first 10 numbers:")
total = 0
for i in range(1, 11):
    total += i
print("Total Sum:", total)
