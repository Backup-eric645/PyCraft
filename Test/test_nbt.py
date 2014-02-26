# -*- coding: utf-8 -*-

"""Check that reading and writing the classic 'bigtest.nbt' file is OK
"""

import unittest
from pycraft import nbt


class BigTest(unittest.TestCase):

    def test_complete(self):
        R = nbt.Reader()
        with open("bigtest.nbt", "rb") as input_file:
            D = R.read(input_file)
            F = R.last_format
            #print(F.pretty(D))

            with open("bigtest.out", "wb") as output_file:
                nbt.write(output_file, D, F)

            input_file.seek(0, 0)
            with open("bigtest.out", "rb") as output_file:
                expected = input_file.read()
                produced = output_file.read()
                self.assertEqual(expected, produced)



if __name__ == "__main__":
    unittest.main()
