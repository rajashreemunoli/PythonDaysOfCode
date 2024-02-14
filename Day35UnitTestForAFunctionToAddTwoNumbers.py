#Write a simple unit test for a function that adds two numbers
def add_two_numbers(a,b):
	return int(a)+int(b)
	
import unittest


class AddTestCase(unittest.TestCase):
	def test_add_numbers(self):
		result=add_two_numbers(10,15)
		self.assertEqual(result,25)

	def test_add_non_numbers(self):
		
		with self.assertRaises(Exception):
			result=add_two_numbers('abc','xyz')

if __name__ == '__main__':
        unittest.main()