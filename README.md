# ♻️ Waste Wise: AI-Powered Waste Segregation & Smart Management System

Waste Wise is a Smart City Web Application that leverages Computer Vision and Deep Learning to automate waste classification, locate nearby recycling hubs, allow public issue reporting, and provide real-time municipal analytics.

## 🚀 Live Demo
- **URL:** [https://waste-wise.streamlit.app](https://waste-wise.streamlit.app) *(Replace with your actual live link)*

## ✨ Key Features
- **📸 AI Garbage Classifier:** Built on **PyTorch MobileNetV2** using Transfer Learning to classify waste into Dry, Wet, Metal, and Paper streams.
- **🗺️ Interactive GIS Recycling Map:** Powered by **Folium & Leaflet.js** to display nearby collection centers across Kalyan, Dombivli, and Nerul.
- **🚨 Citizen Reporting Portal:** Form interface backed by an **SQLite3** relational database with parameterized queries for safe complaint submissions.
- **📊 Municipal Analytics Dashboard:** Interactive data visualizations built using **Pandas & Plotly Express**.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Frontend/Framework:** Streamlit
* **Deep Learning Framework:** PyTorch & Torchvision (`MobileNetV2`)
* **Database:** SQLite3
* **Data Visualization:** Plotly Express & Pandas
* **GIS Mapping:** Folium (`streamlit-folium`)

## 📦 Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/waste-wise.git](https://github.com/YOUR_USERNAME/waste-wise.git)
   cd waste-wise
