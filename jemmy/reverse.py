from collections import namedtuple


class Reverse:
    def decrypt(self, ciphertext, **kwargs):
        return ciphertext[::-1]

    def crack(self, ciphertext, **kwargs):
        result = namedtuple('Result', 'cracked plaintext')
        result.cracked = True
        result.plaintext = self.decrypt(ciphertext, **kwargs)
        return result
