from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from decouple import config

from pysony.feature_extraction import (
    ReverseGeocoder,
    OpenWeatherMap
)

class PipelineUnion(BaseEstimator, TransformerMixin):
    def __init__(self, appid: str, mode: int = 1):
        self.appid = appid
        self.mode = mode
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

class RegrGridSearchCV(BaseEstimator, TransformerMixin):
    def __init__(self, appid: str):
        self.appid = appid
        self.regr = GridSearchCV(
            estimator = Pipeline(
                steps = [
                    ("OpenWeatherMap", OpenWeatherMap(
                        appid = appid
                    )),
                    ("RandomForestRegressor", RandomForestRegressor(
                        n_estimators = 100
                    ))
                ]
            ),
            param_grid = {
                "RandomForestRegressor__min_samples_split": [2,3]
            },
            cv = 3
        )

    def fit(self, X, y = None):
        return self.regr.fit(X,y)
    
    def predict(self, X, y = None):
        return self.regr.predict(X,y)