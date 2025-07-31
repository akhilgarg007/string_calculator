import unittest

from string_calculator import add


class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)

    def test_three_numbers(self):
        self.assertEqual(add("1,2,3"), 6)
    
    def test_new_line_separator(self):
        self.assertEqual(add("1\n2,3"), 6)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringCalculator)
    runner = unittest.TextTestRunner()
    print("Running String Calculator Test Cases...")
    runner.run(suite)
