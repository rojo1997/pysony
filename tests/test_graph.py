import unittest
import numpy as np
from decouple import config

from pysony.graph import GraphDistance

class TestGraphDistance(unittest.TestCase):
    def testGraphDistance(self):
        myGraphDistance = GraphDistance(
            threshold = 20
        )
        X = np.random.rand(10,2) / 2
        X[:,0] += -0.1729636
        X[:,1] += 51.5214588
        node,edge = myGraphDistance.compute(X)
        print(len(node))
        print(len(edge))

if __name__ == '__main__':
    unittest.main(verbosity = 2)