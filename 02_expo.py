import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def expo(n1, n2):
    pass


# DO NOT TOUCH THE BELOW CODE
class TestExpo(unittest.TestCase):

    def test_01(self):
        self.assertEqual(expo(2, 5), 32)

    def test_02(self):
        self.assertEqual(expo(1, 10), 1)

    def test_03(self):
        self.assertEqual(expo(9, 3), 729)


if __name__ == '__main__':
    unittest.main(verbosity=2)
