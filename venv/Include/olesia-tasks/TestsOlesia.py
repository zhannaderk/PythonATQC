#Unit tests to TasksOlesia
import unittest
import TasksOlesia

class Test1 (unittest.TestCase):
    def test_multiple_of_three(self):
        self.assertEqual(TasksOlesia.fizz_buzz(6), 'Fizz')
        self.assertEqual(TasksOlesia.fizz_buzz(5), 'Buzz')
        self.assertEqual(TasksOlesia.fizz_buzz(15), 'FizzBuzz')
        self.assertEqual(TasksOlesia.fizz_buzz(7), '7')

class Test2 (unittest.TestCase):

     def test_profit(self):
        self.assertEqual(TasksOlesia.profit({
                    "cost_price": 32.67,
                    "sell_price": 45.00,
                    "inventory": 1200
                }), 14796)
        self.assertEqual(TasksOlesia.profit({
                    "cost_price": 225.89,
                    "sell_price": 550.00,
                    "inventory": 100
                }), 32411)
        self.assertEqual(TasksOlesia.profit({
                    "cost_price": 2.77,
                    "sell_price": 7.95,
                    "inventory": 8500
                }), 44030)


class Test3 (unittest.TestCase):
    def test_Discriminant(self):
        self.assertEqual(TasksOlesia.solutions(1,2,1), 1)
        self.assertEqual(TasksOlesia.solutions(1,3,1), 2)
        self.assertEqual(TasksOlesia.solutions(2,3,2), 0)

class Test4 (unittest.TestCase):
    def test_square_area(self):
        self.assertEqual(TasksOlesia.square_area(5),50)
        self.assertEqual(TasksOlesia.square_area(6),72)
        self.assertEqual(TasksOlesia.square_area(7),98)

class Test5 (unittest.TestCase):
     def test_list_of_multiplies(self):
        self.assertEqual(TasksOlesia.list_of_multiples(7, 5), [7, 14, 21, 28, 35])
        self.assertEqual(TasksOlesia.list_of_multiples(12, 10), [12, 24, 36, 48, 60, 72, 84, 96, 108, 120])
        self.assertEqual(TasksOlesia.list_of_multiples(17, 6), [17, 34, 51, 68, 85, 102])

class Test6 (unittest.TestCase):
     def test_format_date(self):
        self.assertEqual(TasksOlesia.format_date("11/12/2019"), "20191211")
        self.assertEqual(TasksOlesia.format_date("12/31/2019"), "20193112")
        self.assertEqual(TasksOlesia.format_date("01/15/2019"), "20191501")

class Test7 (unittest.TestCase):
    def test_lines_are_parallel(self):
        self.assertTrue(TasksOlesia.lines_are_parallel([1, 2, 3],[1, 2, 4]))
        self.assertFalse(TasksOlesia.lines_are_parallel([2, 4, 1],[4, 2, 1]))
        self.assertTrue(TasksOlesia.lines_are_parallel([0, 1, 5],[0, 1, 5]))


class Test8(unittest.TestCase):
    def test_vol_shell(self):
        self.assertEqual(TasksOlesia.vol_shell(3, 3), 0)
        self.assertEqual(TasksOlesia.vol_shell(7, 2), 1403.245)
        self.assertEqual(TasksOlesia.vol_shell(3, 800), 2144660471.753)
        self.assertFalse(TasksOlesia.vol_shell(-3, 800))

class Test9(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(TasksOlesia.greeting("Randy"), "Hi! I'm Randy, and I'm from Germany.")
        self.assertEqual(TasksOlesia.greeting("Payl"), "Hi! I'm a guest.")

class Test10(unittest.TestCase):
    def test_stupid_addition(self):
        self.assertEqual(TasksOlesia.stupid_addition(1,2), "12")
        self.assertEqual(TasksOlesia.stupid_addition("1","2"), 3)
        self.assertEqual(TasksOlesia.stupid_addition(1,"2"), None)

class Test11(unittest.TestCase):
    def test_is_repdigit(self):
        self.assertTrue(TasksOlesia.is_repdigit(66))
        self.assertTrue(TasksOlesia.is_repdigit(0))
        self.assertFalse(TasksOlesia.is_repdigit(-11))
        self.assertIn("Error! Invalid value!", TasksOlesia.is_repdigit("test"))

class Test12(unittest.TestCase):
    def test_concat(self):



if __name__ == '__main__':
        unittest.main()


