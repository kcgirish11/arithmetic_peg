import unittest
from arithmetic import evaluate

class TestArithmeticEvaluator(unittest.TestCase):
    
    def test_addition(self):
        expression = "2+3"
        result = evaluate(expression)
        self.assertEqual(result, 5.0)

    def test_subtraction(self):
        expression = "7-4"
        result = evaluate(expression)
        self.assertEqual(result, 3.0)

    def test_multiplication(self):
        expression = "6*3"
        result = evaluate(expression)
        self.assertEqual(result, 18.0)

    def test_division(self):
        expression = "8/2"
        result = evaluate(expression)
        self.assertEqual(result, 4.0)

    def test_combined_operations(self):
        expression = "3+5*2-8/4"
        result = evaluate(expression)
        self.assertEqual(result, 11.0)

    def test_floating_point(self):
        expression = "2.5+3.5"
        result = evaluate(expression)
        self.assertEqual(result, 6.0)

    def test_combined_operations_with_floating_point(self):
        expression = "3.5+2.5*2-1.5/0.5"
        result = evaluate(expression)
        self.assertEqual(result, 5.5)

if __name__ == '__main__':
    unittest.main()
