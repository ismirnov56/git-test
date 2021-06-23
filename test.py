import unittest
from cipher import Cipher

class TestCipher(unittest.TestCase):

    def test_caesar_no_overflow(self):
        text = 'abcd'
        n = 2
        correct = 'cdef'

        result = Cipher.caesar(text, n)
        self.assertEqual(correct, result)

    def test_caesar_overflow(self):
        text = 'abcd'
        n = 25

        result = Cipher.caesar(text, n)


if __name__ == '__main__':
    unittest.main()
