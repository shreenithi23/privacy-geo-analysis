def apply_k_anonymity(df, k=2):
    counts = df.groupby("grid_id").size().reset_index(name="count")

    # Keep only safe grids
    valid_grids = counts[counts["count"] >= k]["grid_id"]

    filtered_df = df[df["grid_id"].isin(valid_grids)].copy()

    return filtered_df