import unittest
import numpy as np
from decouple import config

from pysony.feature_extraction import (
    ReverseGeocoder,
    OpenWeatherMap
)

class TestReverseGeocoder(unittest.TestCase):
    def testReverseGeocoder(self):
        myReverseGeocoder = ReverseGeocoder(mode = 1)
        X = np.random.rand(10,2) / 2
        X[:,0] += -0.1729636
        X[:,1] += 51.5214588
        Y = myReverseGeocoder.transform(X)
        for y in Y[:,1]:
            self.assertEqual(y,"England", msg = "bad location")

class TestOpenWeatherMap(unittest.TestCase):
    def testOpenWeatherMap(self):
        myOpenWeatherMap = OpenWeatherMap(
            appid = config("OPENWEATHERMAP_APIKEY")
        )
        X = np.random.rand(10,2) / 2
        X[:,0] += -0.1729636
        X[:,1] += 51.5214588
        Y = myOpenWeatherMap.transform(X)
        self.assertEqual(Y.shape[1],8, msg = "dimensional error")

if __name__ == '__main__':
    unittest.main(verbosity = 2)