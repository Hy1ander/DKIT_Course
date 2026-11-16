# Exercise 1.2 - Add the numbers between two values

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Put the smaller number first before adding up the range.
if first_number > second_number:
    temp = first_number
    first_number = second_number
    second_number = temp

total = 0

# Add 1 so the end number is included.
for number in range(first_number, second_number + 1):
    total = total + number

print("Total:", total)
