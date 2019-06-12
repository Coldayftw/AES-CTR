import string
import unittest
from aes import AES


def padhexa(s, i):
    return s[2:].zfill(i)


def output_space(s):
    output = ''
    for i in range(len(s) + 1):
        if i % 2 == 0:
            if i > 2:
                output = output + ' '
            output = output + s[i - 2:i]

    return output


def openfile(filename):
    fp = open(filename, 'r')
    lines = fp.readlines()
    fp.close()
    return lines


def hexline(lines):
    s = ''
    for i in range(len(lines)):
        for word in lines[i].split():
            s = s + word.strip(string.whitespace)

    s = '0x' + s
    return int(s, 16)

class AES_TEST(unittest.TestCase):
    def setUp(self):
        lines = openfile('key.txt')
        self.AES = AES(hexline(lines))

    def test_encryption(self):
        print("(for encryption)")
        lines = openfile('en_input.txt')
        lines2 = openfile('ctr.txt')

        encrypted = self.AES.encrypt(int(padhexa(hex(hexline(lines2)), 64)[:32], 16))
        ciphertext = encrypted ^ int(padhexa(hex(hexline(lines)), 64)[:32], 16)
        print(output_space(padhexa(hex(ciphertext), 32)).upper())

        encrypted = self.AES.encrypt(int(padhexa(hex(hexline(lines2)), 64)[32:], 16))
        ciphertext2 = encrypted ^ int(padhexa(hex(hexline(lines)), 64)[32:], 16)
        print(output_space(padhexa(hex(ciphertext2), 32).upper()))

    def test_decryption(self):
        print("(for decryption)")
        lines = openfile('de_input.txt')
        lines2 = openfile('ctr.txt')

        decrypted = self.AES.encrypt(int(padhexa(hex(hexline(lines2)), 64)[:32], 16))
        plaintext = decrypted ^ int(padhexa(hex(hexline(lines)), 64)[:32], 16)
        print(output_space(padhexa(hex(plaintext), 32).upper()))

        decrypted = self.AES.encrypt(int(padhexa(hex(hexline(lines2)), 64)[32:], 16))
        plaintext2 = decrypted ^ int(padhexa(hex(hexline(lines)), 64)[32:], 16)
        print(output_space(padhexa(hex(plaintext2), 32).upper()))


if __name__ == '__main__':
    unittest.main()
