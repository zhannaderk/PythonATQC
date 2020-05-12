## 1. FizzBuzz Interview Question

def fizz_buzz(self, numb):
    if int(numb) % 3 == 0 and int(numb) % 5 == 0:
        return "FizzBuzz"
    elif int(numb) % 3 == 0:
        return "Fizz"
    elif int(numb) % 5 == 0:
        return "Buzz"
    else:
        return str(numb)

# 2. Calculate the Profit
def profit(dict):
    total_sales = dict["sell_price"]*dict["inventory"]
    total_cost = dict["cost_price"]*dict["inventory"]
    return round(total_sales - total_cost)
##
##dd = {"cost_price": float(input("cost_price:")),
##      "sell_price": float(input("sell_price:")), "inventory": int(input("inventory:"))}
##print("Total profit: " , profit(dd))

# 3. How Many Solutions Does This Quadratic Have?

    def solutions(a, b, c):
        D = b * b - 4 * a * c
        if D > 0:
            return 2
        elif D == 0:
            return 1
        else:
            return 0

##a = int(input("a:  " ))
##b = int(input("b:  " ))
##c = int(input("c:  " ))
##if a != 0: print("Quadratic has %s solutions" %(solutions (a, b, c)))
##else: print("This is a linear equation !")

##4. A Circle and Two Squares
def square_area(r):
    if r > 0:
        S = 2*r*r
        return S
    else:
        return None
##try:
##    radius = int(input("Radius:  "))
##    print("Result (the square area of the square inside the circle): %d" %(square_area(radius)))
##except:
##    print("Invalid value was entered !")

### 5. List of Multiples
def list_of_multiples(num, length):
    if length > 0:
        if num != 0:
            lisst = []
            n = num
            for i in range (0, length):
                lisst.insert(i, n)
                n = num+n
            return lisst
        elif num == 0:
            print("Multiple of 0: ")
            return [0]
    else: return "Error! Lenght must be > 0 !"
##
##try:
##    nn = int(input("Num:  " ))
##    ll = int(input("Lenght:  " ))
##    print(list_of_multiples(nn,ll))
##except:
##    print("Invalid value was entered !")