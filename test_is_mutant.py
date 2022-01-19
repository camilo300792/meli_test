import unittest
from is_mutant import is_mutant

class MeliTestCase(unittest.TestCase):

    def test_is_mutant(self):
        dna = ['ATGCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG']
        self.assertTrue(is_mutant(dna))

    def test_is_not_mutant(self):
        dna = ['ATGCGA', 'CAGTGC', 'TTATTT', 'AGACGG', 'GCGTCA', 'TCACTG']
        self.assertFalse(is_mutant(dna))

if __name__ == '__main__':
    unittest.main()