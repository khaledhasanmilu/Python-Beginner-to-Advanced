# Student details
name =input("Enter your name: ")
roll = int(input("Enter your roll: "))
math_marks = 85
science_marks = 78
english_marks = 92
attendance = 82  # in percentage

# Clean name using string functions
name = name.strip().title()

print("Student Name:", name)
print("Roll Number:", roll)

# Total and Average
total_marks = math_marks + science_marks + english_marks
average = total_marks / 3

print("\n--- Marks Summary ---")
print("Math:", math_marks)
print("Science:", science_marks)
print("English:", english_marks)
print("Total:", total_marks)
print("Average:", average)

# Grade based on average
print("\n--- Grade ---")
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)

# Eligibility check (uses logical operators)
print("\n--- Eligibility Check ---")
if average >= 70 and attendance >= 75:
    print("✅ Eligible for certificate and next class promotion")
elif average >= 70 and attendance < 75:
    print("❌ Not eligible due to low attendance")
elif average < 70 and attendance >= 75:
    print("❌ Not eligible due to low marks")
else:
    print("❌ Not eligible due to both low marks and attendance")

# Special message using nested if
if average >= 90:
    if attendance >= 90:
        print("🏆 Excellent Student Award")
    else:
        print("👍 Great marks, but improve attendance")

# Ternary operator for pass/fail
status = "Pass" if average >= 60 else "Fail"
print("\nStatus:", status)

# Extra: Check if name is alphanumeric
print("\n--- Name Check ---")
if name.replace(" ", "").isalnum():
    print("Name is valid (alphanumeric)")
else:
    print("Name is not valid")

