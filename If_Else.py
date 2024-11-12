# Take input and convert it to an integer
try:
    num = int(input("Enter marks: "))
    
    # Check if the marks are within a valid range (e.g., 0-100)
    if 0 <= num <= 100:
        if num > 50:
            print("Pass")
        elif num < 50:
            print("So sad. Fail!")
        else:
            print("Just made it!")
    else:
        print("Please enter a valid mark between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a number.")
