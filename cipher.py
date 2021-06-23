class Cipher:
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    @classmethod
    def get_char(cls, n):
        return cls.alpha[n % 26]


class Caesar(Cipher):
    @classmethod
    def encode(cls, text, n=5):
        res = [Cipher.get_char(cls.alpha.index(c) + n) if c in cls.alpha else c for c in text]
        return ''.join(res)

    @classmethod
    def decode(cls, text, n=5):
        return cls.encode(text, -n)


class Rot13:
    @classmethod
    def encode(cls, text):
        return Caesar.encode(text, 13)

    @classmethod
    def decode(cls, text):
        return cls.encode(text)
