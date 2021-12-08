from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import RobustScaler
from decouple import config

from pysony.feature_extraction import (
    ReverseGeocoder,
    OpenWeatherMap
)

class PipelineUnion(BaseEstimator, TransformerMixin):
    def __init__(self, appid: str, mode: int = 1):
        self.pipeline = FeatureUnion(
            transformer_list = [
                ("ReverseGeocoderPipeline", Pipeline(
                    steps = [
                        ("ReverseGeocoder", ReverseGeocoder(mode = mode))
                    ],
                    verbose = True
                )),
                ("OpenWeatherMapPipeline", Pipeline(
                    steps = [
                        ("OpenWeatherMap", OpenWeatherMap(
                            appid = appid
                        )),
                    ],
                    verbose = True
                ))
            ],
            verbose = True
        )
    
    def fit(self, X, y = None):
        return self

    def transform(self, X, y = None):
        return self.pipeline.transform(X)