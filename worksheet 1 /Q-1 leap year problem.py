'''A year is a leap year under a specific set of rules. You probably remember part of it from school. Write a program that takes a year as input and prints "Leap year" or "Not a leap year".
Test it on: 1900, 2000, 1996, 2023, 2100'''

year= int(input("Enter the year"));
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not leap year")