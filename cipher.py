from itertools import cycle


class Cipher:
    ALPHA = ' abcdefghijklmnopqrstuvwxyz'
    ALPHA_LEN = len(ALPHA)


class Caesar(Cipher):
    @classmethod
    def caesar(cls, text, n):
        result = ''
        for c in text:
            result += cls.ALPHA[(cls.ALPHA.index(c) + n) % cls.ALPHA_LEN]
        return result


class Vigenere(Cipher):
    @classmethod
    def __process(cls, text, key, fn):
        result = ''
        for a, b in zip(text, cycle(key)):
            index = fn(cls.ALPHA.index(a), cls.ALPHA.index(b))
            result += cls.ALPHA[index % cls.ALPHA_LEN]
        return result

    @classmethod
    def decrypt(cls, text, key):
        return cls.__process(text, key, lambda x, y: x - y)

    @classmethod
    def encrypt(cls, text, key):
        return cls.__process(text, key, lambda x, y: x + y)
