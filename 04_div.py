import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def div(n1, n2):
    pass


# DO NOT TOUCH THE BELOW CODE
class TestDiv(unittest.TestCase):

    def test_01(self):
        self.assertEqual(div(3, 5), 0.6)

    def test_02(self):
        self.assertEqual(div(12.5, 10.5), 1.1904761904761905)

    def test_03(self):
        self.assertEqual(div(338, 44), 7.681818181818182)


if __name__ == '__main__':
    unittest.main(verbosity=2)
