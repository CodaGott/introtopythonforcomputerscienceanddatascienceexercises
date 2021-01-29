""" (Sort in Ascending Order) Write a script that inputs three different floating-point
numbers from the user. Display the numbers in increasing order. Recall that an if statement’s
suite can contain more than one statement. Prove that your script works by running it on all six possible
orderings of the numbers. Does your script work with duplicate numbers?
[This is challenging. In later chapters you’ll do this more conveniently and with many more numbers.]"""
largest = 0
second_largest =0
least = 0
first_number = int(input("Enter first number "))
largest = first_number
second_number = int(input("Enter second number "))
if largest < second_number:
    largest = second_number
    second_largest = first_number
    least = first_number
else:
    least = second_number
third_number = int(input("Enter third number "))
if largest < third_number:
    largest = third_number
    if second_largest < third_number:
        second_largest = third_number
        least = second_number
    else:
        least = third_number


print(f"{largest}, {second_largest}, {least}")
# if second_number > first_display and second_number > third_number:
#     second_number = first_display
# elif