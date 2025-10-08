import unittest
from utils import get_max , count_vowels

class TestUtils(unittest.TestCase):
    def test_get_max(self):
        self.assertEqual(get_max([1234567890]), 1234567890)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)
        
if __name__ == '__main__':
    unittest.main()