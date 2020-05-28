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
     def list_of_multiplies_test(self):
            self.assertEqual(TasksOlesia.list_of_multiples(7, 5), [7, 14, 21, 28, 35])
            self.assertEqual(TasksOlesia.list_of_multiples(12, 10), [12, 24, 36, 48, 60, 72, 84, 96, 108, 120])
            self.assertEqual(TasksOlesia.list_of_multiples(17, 6), [17, 34, 51, 68, 85, 102])

class Test6 (unittest.TestCase):
    def format_date_test(self):
        self.assertEqual(TasksOlesia.format_date(11/12/2019), "20191211")
        self.assertEqual(TasksOlesia.format_date(12/31/2019), "20193112")
        self.assertEqual(TasksOlesia.format_date(01/15/2019), "20191501")



if __name__ == '__main__':
    unittest.main()






