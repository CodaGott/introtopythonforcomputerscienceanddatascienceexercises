""" (Separating the Digits in an Integer) Write a script that inputs a five-digit integer
from the user. Separate the number into its individual digits.

Print them separated by three
spaces each. For example, if the user types in the number 42339, the script should print
4 2 3 3 9

Assume that the user enters the correct number of digits. Use both the floor division and
remainder operations to “pick off” each digit."""


number = int(input("Give me 5 digit numbers  "))

if number < 10000 or number > 99999:
    print("Number is greater or less than 5 digits")

last_number = number % 10
number = number // 10

forth_number = number % 10
number = number // 10

third_number = number % 10
number = number // 10

second_number = number % 10
number = number // 10

first_number = number % 10
number = number // 10

print(first_number, second_number, third_number, forth_number, last_number)