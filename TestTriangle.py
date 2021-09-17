# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

#Joseph Letizia
#SSW 567
#HW2

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(2, 5, 6), 'Scalene', '2,5,6 is a scalene triangle')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles', '2,2,3 is a isoceles triangle')

    def testValidation(self):
        self.assertEqual(classifyTriangle(201, 2, 3), 'InvalidInput', 'all ints must be 200 or less')
        self.assertEqual(classifyTriangle(1,2,0), 'InvalidInput', 'all ints must be greater than 0')
        self.assertEqual(classifyTriangle(1,-2,3), 'InvalidInput', 'all ints must be greater than 0')
        self.assertEqual(classifyTriangle("a", 1, 1), 'InvalidInput', 'all inputs must be integers')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(20, 5, 6), 'NotATriangle', 'sum of two sides must be greater than the third side')   
        self.assertEqual(classifyTriangle(11, 5, 6), 'NotATriangle', 'sum of two sides must be greater than the third side')   

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

