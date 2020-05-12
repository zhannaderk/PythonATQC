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