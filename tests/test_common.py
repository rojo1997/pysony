import unittest
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import RobustScaler
from decouple import config

from pysony.feature_extraction import (
    ReverseGeocoder,
    OpenWeatherMap
)

class TestCommon(unittest.TestCase):
    def testCommon(self):
        myReverseGeocoder = ReverseGeocoder(mode = 1)
        X = np.random.rand(10,2) / 2
        X[:,0] += -0.1729636
        X[:,1] += 51.5214588

        pipeline = FeatureUnion(
            transformer_list = [
                ("ReverseGeocoderPipeline", Pipeline(
                    steps = [
                        ("ReverseGeocoder", ReverseGeocoder(mode = 1))
                    ],
                    verbose = True
                )),
                ("OpenWeatherMapPipeline", Pipeline(
                    steps = [
                        ("OpenWeatherMap", OpenWeatherMap(
                            appid = config("OPENWEATHERMAP_APIKEY")
                        )),
                        ("RobustScaler", RobustScaler())
                    ],
                    verbose = True
                ))
            ],
            verbose = True
        )

        pipeline.fit(X, y = [])
        Y = pipeline.transform(X)
        df = pd.DataFrame(Y, columns = ReverseGeocoder.columns + OpenWeatherMap.columns)
        print(df)