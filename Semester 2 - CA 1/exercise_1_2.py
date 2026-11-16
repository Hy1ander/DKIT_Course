# Exercise 1.2 - Add the numbers between two values

first_number = int(input("Enter the smaller number: "))
second_number = int(input("Enter the larger number: "))
total = 0

# Add 1 so the end number is included.
for number in range(first_number, second_number + 1):
    total = total + number

print("Total:", total)
