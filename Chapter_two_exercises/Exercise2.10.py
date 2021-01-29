""" (Arithmetic, Smallest and Largest) Write a script that
inputs three integers from the user.
Display the sum, average, product, smallest and largest of the
numbers. Note that each of these is a reduction
in functional-style programming."""

first_number = int(input("Enter first number"))
second_number = int(input("Enter second number"))
third_number = int(input("Enter third number"))

average = first_number + second_number + third_number / 3
print("average is =", average)

product = first_number * second_number * third_number
print("product is =", product)

smallest_number = first_number

if second_number < first_number:
    smallest_number = second_number
elif third_number < first_number:
    smallest_number = third_number

print("smallest number is =", smallest_number)

largest_number = second_number

if second_number > first_number:
    largest_number = second_number
elif third_number > first_number:
    largest_number = third_number

print("largest number is =", largest_number)