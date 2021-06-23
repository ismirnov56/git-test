import unittest
from cipher import Caesar, Vigenere


class TestCaesar(unittest.TestCase):
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


class TestVigenere(unittest.TestCase):
    text = 'the five boxing wizards jump quickly'
    key = 'hello world'

    def test_encrypt(self):
        code = Vigenere.encrypt(self.text, self.key)
        self.assertNotEqual(code, self.text)
        self.assertEqual(len(code), len(self.text))
        #self.assertCountEqual(self.text, code)

    def test_decrypt(self):
        code = Vigenere.encrypt(self.text, self.key)
        decoded = Vigenere.decrypt(code, self.key)
        self.assertEqual(decoded, self.text)

if __name__ == '__main__':
    unittest.main()
