
from math import pi
from datetime import datetime

# 1. FizzBuzz Interview Question
# Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
#•  If the number is a multiple of 3 the output should be "Fizz".
#•	If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
#•	If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
#•	The output should always be a string even if it is not a multiple of 3 or 5

class FizzBuzz:

    def fizbuzz(n):
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        elif n % 3 == 0 and 0 != n % 5:
            return "Fizz"
        elif n % 3 != 0 and n % 5 == 0:
            return "Buzz"
        else:
            return str(n)

# 2. Calculate the Profit
#You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product.
#You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory.
#Return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold.

class Profit:
    def profit(self, data):
        return round((data['sell_price'] - data['cost_price']) * data['inventory'])


firstSetOfData = {
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
}

secondSetOfData = {
    "cost_price": 225.89,
    "sell_price": 550.00,
    "inventory": 100
}

thridSetOfData = {
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
}

#print(Profit().profit(firstSetOfData))
#print(Profit().profit(secondSetOfData))
#print(Profit().profit(thridSetOfData))

# 3. How Many Solutions Does This Quadratic Have?
# A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct solutions for real values of x.
# Given a, b and c, you should return the number of solutions to the equation.

class Quadratic:
# User inserting the values of a, b and c
#a = int(input("Insert coefficient a: "))
#b = int(input("Insert coefficient b: "))
#c = int(input("Insert coefficient c: "))

    def quadratic (self, a, b, c):
            D = b * b - 4 * a * c
            if D > 0:
                return 2
            elif D == 0:
                return 1
            else:
                return 0

# 4. A Circle and Two Squares
# Imagine a circle and two squares: a smaller and a bigger one.
# For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.
# Create a function, that takes an integer (radius of the circle) and returns the square area of the square inside the circle.

class CircleSquares:


    def square_areas_difference(self, R):
        if R > 0:
            s: int = (2*R^2)
            print(s)
        else:
            return None

# 5. List of Multiples
# Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.
# Examples
# list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
# list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
# list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

class Multiplies:
    def list_of_multiplies(self, num, length):
        arr = []
        for i in range(1, length + 1):
            arr.append(num * i)
        return arr

# print(Multiples().list_of_multiples(7, 5))
# print(Multiples().list_of_multiples(12, 24, 36, 48, 60, 72, 84, 96, 108, 120))
# print(Multiples().list_of_multiples(17, 34, 51, 68, 85, 102))

# 6. Date Format
# Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
# Examples
# format_date("11/12/2019") ➞ "20191211"
#
# format_date("12/31/2019") ➞ "20193112"
#
# format_date("01/15/2019") ➞ "20191501"
# Notes
# Return value should be a string.'''


class NewDateFormat:

    oldformat1 = '11/12/2019'
    oldformat2 = '12/31/2019'
    oldformat3 = '01/15/2019'
    datetimeold1 = datetime.strptime(oldformat1,'%m/%d/%Y')
    datetimeold2 = datetime.strptime(oldformat2,'%m/%d/%Y')
    datetimeold3 = datetime.strptime(oldformat3,'%m/%d/%Y')
    newformat1 = datetimeold1.strftime('%m%d%Y')
    newformat2 = datetimeold2.strftime('%m%d%Y')
    newformat3 = datetimeold3.strftime('%m%d%Y')
    #print (newformat1, newformat2, newformat3)

# 7. Check If Lines Are Parallel
# Given two lines, determine whether or not they are parallel.
# Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.
# Examples
# lines_are_parallel([1, 2, 3], [1, 2, 4]) ➞ true
# x+2y=3 and x+2y=4 are parallel.

# lines_are_parallel([2, 4, 1], [4, 2, 1]) ➞ false
# 2x+4y=1 and 4x+2y=1 are not parallel.

# lines_are_parallel([0, 1, 5], [0, 1, 5]) ➞ true
# Lines are parallel to themselves.
# Notes
# All the coefficients will be integers (whole numbers).

class ParallelLines:

    def lines_are_parallel (self, line1, line2):
        return line1[0]/line1[1]==line2[0]/line2[1]

# print(ParallelLines().lines_are_parallel(line1=[1,2,3],line2=[2,3,4]) )

# 8. Volume of a Spherical Shell
# The volume of a spherical shell is the difference between the enclosed volume of the outer sphere and the enclosed volume of the inner sphere:
# Create a function that takes r1 and r2 as arguments and returns the volume of a spherical shell rounded to the nearest thousandth.
# Notes
# The inputs are always positive numbers. r1 could be the inner radius or the outer radius, don't return a negative number.

class Volume:
    def vol_spher_shell(r1, r2):
        if r1 <= 0:
            return None
        else: v = 4/3*pi*r1**3 - 4/3*pi*r2**3
        return (round(v,3))
# print(vol_spher_shell(5, 3))

# 9. International Greetings
# Suppose you have a guest list of students and the country they are from, stored as key-value pairs in a dictionary.
# GUEST_LIST = {
# "Randy": "Germany",
# "Karla": "France",
# "Wendy": "Japan",
# "Norman": "England",
# "Sam": "Argentina"
# }
# Write a function that takes in a name and returns a name tag, that should read:
# "Hi! I'm [name], and I'm from [country]."
# If the name is not in the dictionary, return:
# "Hi! I'm a guest."

class GuestList:
    guest_list = {
        "Randy": "Germany",
        "Karla": "France",
        "Wendy": "Japan",
        "Norman": "England",
        "Sam": "Argentina"
    }
    def guestcheck (name):
        if name not in guest_list.keys:
            return ("Hi! I'm a guest.")
        else:
            return ("Hi! I'm %s, and I'm from %s." % (name, guest_list.get(name)))


# Create a function that takes two parameters and, if both parameters are strings,
# add them as if they were integers or if the two parameters are integers, concatenate them.
# Examples
# stupid_addition(1, 2) ➞ "12"
# stupid_addition("1", "2") ➞ 3
# stupid_addition("1", 2) ➞ None
# Notes
# If the two parameters are different data types, return None.
# All parameters will either be strings or integers.

class Stupid:
    def stupid_addition(a, b):
        isAString = isinstance(a, str)
        isBString = isinstance(b, str)
        if isAString and isBString:
         return int(a) + int(b)
        elif isAString or isBString:
         return None
        else:
         return str(a) + str(b)

# print(stupid_addition(1, 2))
# print(stupid_addition(1, "2"))
# print(stupid_addition("1", "2"))

# 11. Is the Number a Repdigit
# A repdigit is a positive number composed out of the same digit.
# Create a function that takes an integer and returns whether it's a repdigit or not.
# Examples
# is_repdigit(66) ➞ True
# is_repdigit(0) ➞ True
# is_repdigit(-11) ➞ False
# Notes
# The number 0 should return True (even though it's not a positive number).

class Repdigit ():
    def is_repdigit(x):
        if x == 0:
            return True
        y = str(x)
        for i in range(1, len(y)):
            if y[0] == y[i]:
                return True
            else:
                return False















