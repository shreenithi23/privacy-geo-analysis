import pandas as pd
import numpy as np

np.random.seed(42)

# Bangalore center
CENTER_LAT = 12.9716
CENTER_LON = 77.5946

NUM_POINTS = 5000

data = []

# Create clusters (simulate real city zones)
clusters = [
    (12.97, 77.59),   # central
    (12.98, 77.60),   # east
    (12.96, 77.58),   # west
    (12.99, 77.61),   # north
]

for i in range(NUM_POINTS):
    cluster = clusters[np.random.randint(0, len(clusters))]

    lat = np.random.normal(cluster[0], 0.003)
    lon = np.random.normal(cluster[1], 0.003)

    income = np.random.randint(20000, 100000)

    data.append([i, lat, lon, income])

df = pd.DataFrame(data, columns=["user_id", "latitude", "longitude", "income"])

df.to_csv("locations.csv", index=False)

print("✅ Dataset generated: 500 points")