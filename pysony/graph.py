from geopy.distance import geodesic
import numpy as np

class GraphDistance:
    def __init__(self, threshold: float = 5):
        self.threshold = threshold

    def compute(self, X: np.ndarray):
        node = []
        edge = []

        for x in X:
            node.append({
                "_key": str(hash(str(x[0]) + str(x[1]))),
                "lon": x[0],
                "lat": x[1],
            })
        for i,x1 in enumerate(X):
            for j,x2 in enumerate(X):
                if i != j:
                    distance = geodesic(
                        (x1[1],x1[0]),
                        (x2[1],x2[0]),
                    ).km
                    if distance < self.threshold:
                        x1_hash = str(hash(str(x1[0]) + str(x1[1])))
                        x2_hash = str(hash(str(x2[0]) + str(x2[1])))
                        edge.append({
                            "_from": "node/" + x1_hash,
                            "_to": "node/" + x2_hash,
                            "distance": distance
                        })
        return node,edge
