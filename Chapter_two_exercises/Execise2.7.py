""" (Multiples) Use if statements to determine whether 1024 is
a multiple of 4 and
whether 2 is a multiple of 10.
(Hint: Use the remainder operator.)"""

number = int(input("Enter a number here!  "))
multiples = int(input("Enter a multiples number "))

if number % multiples == 0:
    print(number, "is a multiples of", multiples)
else:
    print(number, "is not a multiple of ", multiples)