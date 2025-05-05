import os
import streamlit as st
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

# --- Konfigurasi Kaggle dari Streamlit Secrets ---
os.environ["KAGGLE_USERNAME"] = st.secrets["kaggle"]["username"]
os.environ["KAGGLE_KEY"] = st.secrets["kaggle"]["key"]

# --- Autentikasi API ---
api = KaggleApi()
api.authenticate()

# --- Fungsi untuk mendownload dataset ---
@st.cache_data
def download_dataset():
    dataset_name = "fedesoriano/cirrhosis-prediction-dataset"
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)
    api.dataset_download_files(dataset_name, path=output_dir, unzip=True)
    return os.path.join(output_dir, "cirrhosis.csv")

# --- Download & load data ---
csv_path = download_dataset()
df = pd.read_csv(csv_path)

# --- Tampilan Aplikasi ---
st.title("Cirrhosis Prediction Dataset Viewer")
st.markdown("Dataset ini berisi data pasien dengan penyakit hati kronis untuk analisis atau prediksi sirosis hati.")

st.subheader("🔍 Data Preview")
st.dataframe(df.head())

st.subheader("📊 Statistik Ringkas")
st.write(df.describe())

st.subheader("📌 Kolom Tersedia")
st.write(list(df.columns))
