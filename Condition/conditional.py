# Define test values
x = 10
y = 20
z = 5

# 1. Simple if
if x > 5:
    print("1. 'if' => x is greater than 5")

# 2. if...else
if y < 15:
    print("2. 'if-else' => y is less than 15")
else:
    print("2. 'if-else' => y is not less than 15")

# 3. if...elif...else
if z > 10:
    print("3. 'if-elif-else' => z is greater than 10")
elif z == 5:
    print("3. 'if-elif-else' => z is equal to 5")
else:
    print("3. 'if-elif-else' => z is less than 5")

# 4. Nested if
if x > 5:
    if y > 15:
        print("4. Nested if => x > 5 and y > 15")

# 5. Ternary (one-line if)
result = "Even" if x % 2 == 0 else "Odd"
print("5. Ternary => x is", result)

# 6. Logical operators
if x > 5 and y > 15:
    print("6. Logical AND => Both x > 5 and y > 15 are True")

if x < 5 or z == 5:
    print("6. Logical OR => At least one condition is True")

if not (z > 10):
    print("6. Logical NOT => z is not greater than 10")

# 7. Comparison operators
print("7. Comparisons:")
print("   x == 10:", x == 10)
print("   y != 15:", y != 15)
print("   x >= y:", x >= y)
print("   z < x:", z < x)

