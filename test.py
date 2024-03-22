import unittest
from main import power
class MathsTestFunction(unittest.TestCase):
    """Tests for power"""
    def test_power(self):
        """Do values like 2, 3 work?"""
        X= power(2, 3)
        self.assertEqual(X, 8)
unittest.main()

import unittest
from main import factorial
class MathsTestFunction(unittest.TestCase):
    """Tests for factorial"""
    def test_factorial(self):
        """Do values like 5 work?"""
        Y= factorial(5)
        self.assertEqual(Y, 120)
unittest.main()

import unittest
from main import permutation
class MathsTestFunction(unittest.TestCase):
    """Tests for permutation"""
    def test_permutation(self):
        """Do values like 5, 2 work?"""
        Z= permutation(5, 2)
        self.assertEqual(Z, 20)
unittest.main()

import unittest
from main import combination
class MathsTestFunction(unittest.TestCase):
    """Tests for combination"""
    def test_combination(self):
        """Do values like 5, 2 work?"""
        A= combination(5, 2)
        self.assertEqual(A, 10)
unittest.main()