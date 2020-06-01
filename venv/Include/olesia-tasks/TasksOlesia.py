from math import pi
from datetime import datetime

## 1. FizzBuzz Interview Question

def fizz_buzz(numb):
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


###6. Date Format
def format_date(date):
    mdy = date.split("/")
    if len(mdy) == 3:
        if mdy[2].isdigit() == True and mdy[1].isdigit() == True and mdy[0].isdigit() == True:
            if len(str(mdy[2])) == 4 and len(str(mdy[1])) == 2 and len(str(mdy[0])) == 2:
                return str(mdy[2]) + str(mdy[1]) + str(mdy[0])
            else:
                return "Error! Date was entered in invalid format ! "
        else:
            return "Error! Invalid value(s) was(were) entered ! "
    else:
        return "Error! Date was entered in invalid format hasjkdfhajkdfhalhdfajk! "


##
##mmddyy = input("Please enter a Date in MM/DD/YYYY format: ")
##print("Result in YYYYDDMM format: %s" %(format_date(mmddyy)))

# 7. Check If Lines Are Parallel
def lines_are_parallel(list1, list2):
    if len(list2) != 3 and len(list1) != 3: return "Error! "
    temp = []
    for i in range(0, 2):
        if list2[i] == 0 and list1[i] != 0:
            return False
        elif list2[i] == 0 and list1[i] == 0:
            return True
        temp.append(list1[i] / list2[i])
    if temp[0] == temp[1]:
        return True
    else:
        return False


# list_1 = list(input("1 Line is represented by a list [a, b, c]. Please enter values separated by a space: "))
# list_2 = list(input("2 Line is represented by a list [a, b, c]. Please enter values separated by a space: "))
# print(lines_are_parallel(list_1, list_2))
# print(lines_are_parallel([1,2,3], [1,2,4]))

# 8. Volume of a Spherical Shell
def vol_shell(r1, r2):
    if r1 >= r2:
        vol = round((4 / 3 * pi * r1 ** 3 - 4 / 3 * pi * r2 ** 3), 3)
    else:
        vol = round((4 / 3 * pi * r2 ** 3 - 4 / 3 * pi * r1 ** 3), 3)
    return vol


##r1 = int(input("R1:  " ))
##r2 = int(input("R2:  " ))
##print(vol_shell(r1, r2))

# 9. International Greetings
GUEST_LIST = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina"
}


def greeting(name):
    if name not in GUEST_LIST:
        return print("Hi! I'm a guest.")
    else:
        return print("Hi! I'm %s, and I'm from %s." % (name, GUEST_LIST.get(name)))


# greeting("Karla")

# 10. Stupid Addition
def stupid_addition(n1, n2):
    if type(n1) == int and type(n2) == int:
        return str(n1) + str(n2)
    elif type(n1) == str and type(n2) == str:
        if n1.isdigit() == True and n2.isdigit() == True:
            return int(n1) + int(n2)
        else:
            return "Error! Incorrect value(s)!"
    elif type(n1) == type(n2) and type(n1) != (int or srt):
        return "Error! Incorrect value(s)!!"
    else:
        return None


##print(stupid_addition(1.2, 7.7))
##print("*************")
##print(stupid_addition(1, 7))
##print("*************")
##print(stupid_addition("1", "7"))
##print("*************")
##print(stupid_addition(4, "7"))
##print("*************")
##print(stupid_addition(True, True))
##print("*************")
##print(stupid_addition(1+3J, 1+3J))
##print("*************")
##print(stupid_addition("4.1", "7.7"))
##print("*************")
##print(stupid_addition("aa", "#@"))
##print("*************")
##print(stupid_addition(3, "h"))

# 11. Is the Number a Repdigit
def is_repdigit(numb):
    if type(numb) != int: return "Error! Invalid value!"
    s_numb = str(numb)
    return int(numb) >= 0 and s_numb.replace(s_numb[0], "") == ""


#print(is_repdigit(88888))
##print(is_repdigit(8))
##print(is_repdigit(88488))
##print(is_repdigit(0))
##print(is_repdigit(-44))
##print(is_repdigit("a"))
##print(is_repdigit(5.5))

##12. Concatenate Variable Number of Input Lists
##Create a function that concatenates n input lists, where n is variable
def concat(*n_lists):
    temp = []
    for i in range(len(n_lists)):
        temp = temp + n_lists[i]
    return temp


##print(concat([1], [2], [3], [4], [5], [6], [7]))
##print(concat([1]))

##13. Emptying the values
##Given a list of values, return a list with each value replaced with the empty value of the same type
def replacing(lisst):
    types_dict = {int: 0, float: 0.0, str: '', bool: False, list: [], tuple: (), set: set(), type(None): None, dict: {}}
    temp_types = []
    res_list = []
    for i in range(len(lisst)):
        temp_types.append(type(lisst[i]))
    for i in range(len(temp_types)):
        if temp_types[i] in types_dict:
            res_list.append(types_dict[temp_types[i]])
        else:
            return "Error! Incorrect value's type!"
    return res_list


##print(replacing([1, 2, 5.05, "test", True, [5,7,9], (7,7,7), {"a","b"}, None, () ]))

##14. Sum Fractions
##Create a function that takes a list containing nested lists as an argument.
##Each sublist has 2 elements. The first element is the numerator and
##the second element is the denominator. Return the sum of the fractions rounded to the nearest whole number.
def sum_fractions(lisst):
    temp = []
    summ = 0
    for i in range(len(lisst)):
        if type(lisst[i]) != list: return "Error! The Argument must be a list with nested lists!"
        if len(lisst[i]) != 2: return "Error! Each sublist must have 2 elements!"
        for j in range(len(lisst[i])):
            temp.append(lisst[i][j])
    i = 0
    while i < len(temp):
        if temp[i + 1] == 0:
            return "Error! Division by zero is not allowed!"
        else:
            summ += temp[i] / temp[i + 1]
            i += 2
    return round(summ)


##print(sum_fractions([ [11, 2], [3, 4], [5, 4], [21, 11], [12, 6] ]))

# 15. All Occurrences of an Element in a List
def get_indices(lisst, item):
    if lisst.count(item) == 0: return []
    indexes = set()
    for i in range(len(lisst)):
        try:
            indexes.add(lisst.index(item, 0 + i))
        except ValueError:
            break
    return list(indexes)
##print(get_indices([1,"a",-2,"b", 8.8, "c"], "c"))