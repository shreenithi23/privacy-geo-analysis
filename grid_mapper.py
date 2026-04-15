import math

GRID_SIZE = 0.01  # ~1km (approx)

def get_grid_id(lat, lon):
    lat_grid = math.floor(lat / GRID_SIZE)
    lon_grid = math.floor(lon / GRID_SIZE)
    return f"{lat_grid}_{lon_grid}"

def assign_grids(df):
    df["grid_id"] = df.apply(
        lambda row: get_grid_id(row["latitude"], row["longitude"]),
        axis=1
    )
    return df