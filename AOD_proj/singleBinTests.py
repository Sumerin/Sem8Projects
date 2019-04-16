import binPacking
import unittest

class BinPackingTest(unittest.TestCase):

    def test_1(self):
        weight = [1, 2, 2]
        bincapicity = 2
        maxBins = 20

        usedBins = binPacking.binPacking(weight, bincapicity, maxBins)

        self.assertEqual(3, usedBins)

    def test_2(self):
        weight = [2, 2, 2]
        bincapicity = 3
        maxBins = 4

        usedBins = binPacking.binPacking(weight, bincapicity, maxBins)

        self.assertEqual(3, usedBins)

    def test_NoSolution(self):#prints warning to STDERR
        weight = [2, 2, 2]
        bincapicity = 3
        maxBins = 1

        usedBins = binPacking.binPacking(weight, bincapicity, maxBins)

        self.assertEqual(0, usedBins)

    def test_4(self):
        weight = [2.5, 2.5, 4]
        bincapicity = 5
        maxBins = 4

        usedBins = binPacking.binPacking(weight, bincapicity, maxBins)

        self.assertEqual(2, usedBins)

    def test_5(self):
        weight = [4, 8, 1, 4, 2, 1]
        bincapicity = 10
        maxBins = 4

        usedBins = binPacking.binPacking(weight, bincapicity, maxBins)

        self.assertEqual(2, usedBins)

    def test_6(self):
        weight = [9, 8, 2, 2, 5, 4]
        bincapicity = 10
        maxBins = 5

        usedBins = binPacking.binPacking(weight, bincapicity, maxBins)

        self.assertEqual(4, usedBins)

    def test_7(self):
        weight = [2, 5, 4, 7, 1, 3, 8]
        bincapicity = 10
        maxBins = 5

        usedBins = binPacking.binPacking(weight, bincapicity, maxBins)

        self.assertEqual(3, usedBins)

    def test_8(self):
        weight = [2, 2, 2, 4, 4, 4]
        bincapicity = 6
        maxBins = 6

        usedBins = binPacking.binPacking(weight, bincapicity, maxBins)

        self.assertEqual(3, usedBins)

    def test_9(self):
        weight = [2, 2, 2, 4, 4, 4]
        bincapicity = 5
        maxBins = 6

        usedBins = binPacking.binPacking(weight, bincapicity, maxBins)

        self.assertEqual(5, usedBins)

    def test_10_with_debug(self):
        weight = [18, 21, 2, 48, 58, 42]
        bincapicity = 60
        maxBins = 25

        usedBins = binPacking.binPacking(weight, bincapicity, maxBins, True)

        self.assertEqual(4, usedBins)