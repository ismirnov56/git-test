import unittest
from cipher import Caesar


class TestCipher(unittest.TestCase):
    text = 'the quick brown fox jumps over the lazy dog'

    def test_caesar_encode(self):
        encoded = Caesar.encode(self.text)
        self.assertNotEqual(encoded, self.text)  # Закодированный текст отличается от исходого
        self.assertEqual(len(encoded), len(self.text))  # Длина закодированного и исходного текста совпадает

    def test_caesar_decode(self):
        encoded = Caesar.encode(self.text)
        decoded = Caesar.decode(encoded)
        self.assertEqual(decoded, self.text)  # Раскодированный шифр совпадает с исходным текстом


if __name__ == '__main__':
    unittest.main()
