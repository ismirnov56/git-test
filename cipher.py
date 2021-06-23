class Caesar:
    alpha = ' abcdefghijklmnopqrstuvwxyz'
    alphalen = len(alpha)

    @classmethod
    def encode(cls, text, n=5):
        res = ''
        for c in text:
            res += cls.alpha[(cls.alpha.index(c) + n) % cls.alphalen]
        return res

    @classmethod
    def decode(cls, text, n=5):
        return cls.encode(text, -n)
