class QueryEngine:

    def __init__(self, df):
        self.df = df

    def count(self, grid_id):
        return int(self.df[self.df["grid_id"] == grid_id].shape[0])

    def average_income(self, grid_id):
        subset = self.df[self.df["grid_id"] == grid_id]
        if subset.empty:
            return None
        return float(subset["income"].mean())

    def get_all_grids(self):
        return self.df["grid_id"].unique().tolist()