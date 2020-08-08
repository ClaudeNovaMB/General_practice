import unittest
import Unit_testing_code

class CapitalizerTester(unittest.TestCase):
	
    def test_one_word(self):
        text = 'finance'
        output = Unit_testing_code.capitalizer(text)
        self.assertEqual(output, 'Finance')

    def test_multiple_words(self):
        text = 'finance is great'
        output = Unit_testing_code.capitalizer(text)
        self.assertEqual(output, 'Finance Is Great')

if __name__ == "__main__":
    unittest.main()
