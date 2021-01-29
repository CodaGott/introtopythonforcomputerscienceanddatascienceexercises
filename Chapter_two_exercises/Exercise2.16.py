first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

third_number = int(input("Enter third number: "))

max_number = first_number
min_number = first_number
mid_number = first_number


if first_number > second_number and first_number > third_number:
    max_number = first_number

if second_number < max_number and second_number > third_number:
    mid_number = second_number

if third_number < mid_number and third_number < max_number:
    min_number = third_number




print(max_number, mid_number, min_number)