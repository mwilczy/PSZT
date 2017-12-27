import unittest

from project.Chromosome import Chromosome


class TestChromosomeClass(unittest.TestCase):
    def testCase(self):
        testChromosome = Chromosome([1, 5, 115])
        self.assertTrue(testChromosome.calculateIndexes() == [1,5,115])

        testChromosome = Chromosome([515, 54, 1])
        self.assertTrue(testChromosome.calculateIndexes() == [1, 54, 515])

        with self.assertRaises(IndexError):
            testChromosome = Chromosome([515, 54, -1])



if (__name__ == '__main__'):
    unittest.main()



