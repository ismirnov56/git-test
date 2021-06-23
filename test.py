import unittest
from cipher import Caesar


class TestCipher(unittest.TestCase):
    def test_caesar_no_overflow(self):
        text = 'abcd'
        n = 2
        correct = 'cdef'

        result = Caesar.caesar(text, n)
        self.assertEqual(correct, result)

    def test_caesar_overflow(self):
        text = 'abcd'
        n = 25

        result = Caesar.caesar(text, n)


if __name__ == '__main__':
    unittest.main()
