from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import RobustScaler
from decouple import config

from pysony.feature_extraction import (
    ReverseGeocoder,
    OpenWeatherMap
)

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
            ],
            verbose = True
        ))
    ],
    verbose = True
)