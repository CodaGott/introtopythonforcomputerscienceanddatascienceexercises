# product = 7

# while product <= 1_000_000:
#     product = product * 7
#     print(product)
    
# for character in "programming":
#     print(character, end=' ')
#
# print("\n")
#
# for num in range(1, 11):
#     print(num, end=" ")
#
# for num in range(1_000_000_1):
#     if num == 1_000_000:
#         break
#
#     print(num)

# total = 0
# grade_counter = 0
#
# grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
# for grade in grades:
#     total += grade
#     grade_counter += 1
#
# average = total / grade_counter
#
# print("the average result is", average,"and the total is",total)

# for num in [122, 789, 687, 67]:
#     total += num
#
# print(total)
#
# x = 12
#
# x **= 2
# print(x)

# number = 10
#
# for num in range(0, number):
#     for printer in range(num):
#         print("*", end=" ")
#     print()

# total = 0
# grade_counter = 0
#
# grade = int(input("Enter grade or press -1 to exit: "))
#
# while grade != -1:
#     total += grade
#     grade_counter += 1
#     grade = int(input("Enter grade or press -1 to exit: "))
#
# if grade_counter != 0:
#     average = total / grade_counter
#     print(f"Average for the class is {average:.2f}")
# else:
#     print("No grades were entered")

# passes = 0
# failures = 0
#
# for scores in range(10):
#     result = int(input("enter score "))
#
#     if result == 1:
#         passes += 1
#     else:
#         failures += 1
# print()
#
# print("Number of passes is", passes)
# print("Number of failures", failures)
#
# print()
#
# if passes >= 8:
#     print("Bonus to the instructor")

# for count in range(2):
#     value = int(input("Enter an integer: "))
#
#     if value % 2 == 0:
#         print(f"{value} is even")
#     else:
#         print(f"{value} is odd")

from decimal import Decimal
import statistics

# sum = 0
# for num in range(2, 100):
#     sum += num
#     print(sum)
#
# print()
# print(sum)

# p = Decimal(99.00)
# add = Decimal(1.00)
#
# print("new",p + add)

p = Decimal(1000.00)
r = Decimal(0.05)
n = 10

print("year earnings")

for years in range (1, 101):
    a = p * (1 + r) ** years
    print(f"{years:>2}{a:>10.2f}")
print()

total = Decimal(0)
amout_spent = Decimal(37.45)
per = amout_spent * Decimal(0.0625)

print(f"{per:>.2f}")

grades = [85, 93, 45, 45, 45, 45, 89, 85]

print("mean is ",statistics.mean(grades))

print("median is ",statistics.median(grades))

print("mode is ",statistics.mode(grades))

print("sorted grades", sorted(grades))