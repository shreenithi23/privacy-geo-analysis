# 🔐 Privacy-Preserving Geospatial Analytics System

## 📌 Overview

This project is a **privacy-preserving geospatial analytics platform** that enables analysis of location-based data while protecting individual user privacy. It combines **geospatial modeling, data aggregation, and privacy mechanisms** to ensure that sensitive location information is never exposed.

The system converts raw latitude and longitude data into grid-based regions and allows only **aggregated queries** on safe regions, preventing re-identification of individuals.

---

## 🚀 Features

- 📍 Grid-based spatial modeling (lat/lon → grid_id)
- 🔐 Privacy enforcement using **k-anonymity**
- 🚫 Suppression of unsafe regions
- 📊 Aggregated query system (count, average)
- ⛔ Query rate limiting (prevents inference attacks)
- 🌐 FastAPI backend (REST APIs)
- 🗺️ Interactive map visualization (Leaflet)
- 🔥 Heatmap for hotspot detection
- 📊 Dashboard panel showing grid statistics
- 🔄 Toggle heatmap ON/OFF
- ⚖️ Demonstrates **privacy vs utility tradeoff**

---

## 🧠 How It Works

1. **Data Ingestion**
   - Input dataset: latitude, longitude, income

2. **Spatial Discretization**
   - Converts coordinates → fixed grid cells

3. **Aggregation**
   - Groups data by grid_id
   - Computes count and average income

4. **Privacy Enforcement**
   - Applies k-anonymity:
     - Safe → count ≥ K
     - Unsafe → count < K

5. **Query System**
   - Only aggregated queries allowed
   - Unsafe grids are blocked

6. **Visualization**
   - Grid map (discrete)
   - Heatmap (continuous)
   - Stats panel (table view)

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Pandas

### Frontend
- HTML, CSS, JavaScript
- Leaflet.js (maps)
- Leaflet Heatmap plugin

---

## ▶️ Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd project
```

### 2. Install dependencies 
```bash
pip install fastapi uvicorn pandas
```
### 3. Run backend
```bash
uvicorn api.main:app --reload
```

### 4. Run frontend
```bash
cd frontend
python -m http.server 5500
```

### OPen in browser
http://localhost:5500/index.html

## 🧪 Testing

Use Swagger UI:

http://127.0.0.1:8000/docs

Test:
- Valid queries (count, avg)
- Unsafe grid queries (should fail)
- Invalid inputs

---

## 🔐 Privacy Mechanisms

- Grid-based anonymization  
- k-anonymity enforcement  
- Query access control  
- Rate limiting  

---

## 🌍 Geospatial Analysis

- Spatial discretization (grid mapping)  
- Density analysis  
- Hotspot detection (heatmap)  
- Spatial visualization (grid + heatmap)  

---

## ⚡ Big Data Concepts

- Large dataset handling (10K+ records)  
- Efficient aggregation (groupby)  
- Optimized lookup (O(1) dictionary)  
- Scalable pipeline design  

---

## 📈 Future Improvements

- Apache Spark integration (true big data)  
- Real-world datasets (OpenStreetMap)  
- Differential privacy (noise addition)  
- Time-based analysis (spatio-temporal)  
- React dashboard UI  

---

## 🎯 Key Concept

**Privacy vs Utility Tradeoff**

- Safe grids → usable data  
- Unsafe grids → hidden for privacy  