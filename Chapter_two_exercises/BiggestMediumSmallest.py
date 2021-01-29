first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

third_number = int(input("Enter third number: "))

# max_number = first_number
# 
# min_number = first_number
# 
# mid_number = first_number

if first_number > second_number and first_number > third_number:
    max_number = first_number
elif second_number > first_number and second_number > third_number:
    max_number = second_number
else:
    max_number = third_number

print(max_number)

if first_number < second_number and first_number < third_number:
    min_number = first_number
elif second_number < first_number and second_number < third_number:
    min_number = second_number
else:
    min_number = third_number

print(min_number)

if first_number > second_number and first_number < third_number:
    middle_number = first_number
elif second_number > first_number and second_number < third_number:
    middle_number = second_number
elif third_number > first_number and third_number < second_number:
    middle_number = third_number
print(middle_number)