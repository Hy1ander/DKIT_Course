# Exercise 1.1 - Sum and average

total = 0
count = 0
number = float(input("Enter a number (-1 to stop): "))

# Check for -1 before adding the number.
while number != -1:
    total = total + number
    count = count + 1
    number = float(input("Enter a number (-1 to stop): "))

print("Sum:", total)

# Avoid dividing by zero if -1 is entered first.
if count == 0:
    print("Average: no numbers were entered.")
else:
    average = total / count
    print("Average:", average)
