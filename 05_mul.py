import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def mul(n1, n2):
    return(n1*n2)


# DO NOT TOUCH THE BELOW CODE
class TestMul(unittest.TestCase):

    def test_01(self):
        self.assertEqual(mul(3, 5), 15)

    def test_02(self):
        self.assertEqual(mul(12, 10), 120)

    def test_03(self):
        self.assertEqual(mul(33, 44), 1452)


if __name__ == '__main__':
    unittest.main(verbosity=2)
