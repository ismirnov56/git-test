class Cipher:
    alpha = ' abcdefghijklmnopqrstuvwxyz'
    alphalen = len(alpha)

    @classmethod
    def caesar(cls, text, n):
        res = ''
        for c in text:
            res += cls.alpha[cls.alpha.index(c) + n]
        return res
