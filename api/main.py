from fastapi import FastAPI, HTTPException
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse


from grid_mapper import assign_grids
from query_limiter import QueryLimiter

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Config ----------------
GRID_SIZE = 0.01
K = 5

# ---------------- Load Data ----------------
df = pd.read_csv("locations.csv")

# Assign grids
df = assign_grids(df)

# Compute counts (DO NOT FILTER)
# Precompute once
counts = df.groupby("grid_id").size().reset_index(name="count").copy()
counts["safe"] = counts["count"] >= K

# Cache for fast lookup
counts_dict = counts.set_index("grid_id").to_dict("index")

limiter = QueryLimiter()

# ---------------- Routes ----------------

@app.get("/")
def home():
    return {"message": "Privacy-Preserving Geo Query System"}


@app.get("/grids")
def get_grids():
    return {"grids": counts["grid_id"].tolist()}


# ---------------- Query (SAFE ONLY) ----------------
@app.post("/query")
def query(user_id: int, grid_id: str, operation: str):

    # Rate limiting
    if not limiter.allow(user_id):
        raise HTTPException(status_code=403, detail="Query limit exceeded")

    # Get grid (dict lookup)
    grid_row = counts_dict.get(grid_id)

    if grid_row is None:
        raise HTTPException(status_code=404, detail="Grid not found")

    # Check privacy
    if not grid_row["safe"]:
        raise HTTPException(
            status_code=403,
            detail="Grid suppressed due to k-anonymity"
        )

    # Perform aggregation
    subset = df[df["grid_id"] == grid_id]

    if operation == "count":
        return {"result": int(subset.shape[0])}

    elif operation == "avg_income":
        return {"result": float(subset["income"].mean())}

    else:
        raise HTTPException(status_code=400, detail="Invalid operation")


# ---------------- Stats (ALL GRIDS) ----------------
@app.get("/stats", response_class=HTMLResponse)
def stats():
    rows = ""

    for _, row in counts.iterrows():
        color = "gray" if not row["safe"] else "green"

        rows += f"""
        <tr>
            <td>{row['grid_id']}</td>
            <td>{row['count']}</td>
            <td style="color:{color}; font-weight:bold;">
                {"SAFE" if row["safe"] else "SUPPRESSED"}
            </td>
        </tr>
        """

    html_content = f"""
    <html>
    <head>
        <title>Grid Statistics</title>
        <style>
            body {{
                font-family: Arial;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            h2 {{
                text-align: center;
            }}
            table {{
                border-collapse: collapse;
                width: 80%;
                margin: auto;
                background: white;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            th, td {{
                padding: 12px;
                border: 1px solid #ddd;
                text-align: center;
            }}
            th {{
                background-color: #333;
                color: white;
            }}
            tr:hover {{
                background-color: #f1f1f1;
            }}
        </style>
    </head>
    <body>

        <h2>📊 Grid Statistics Dashboard</h2>

        <table>
            <tr>
                <th>Grid ID</th>
                <th>User Count</th>
                <th>Status</th>
            </tr>
            {rows}
        </table>

    </body>
    </html>
    """

    return html_content