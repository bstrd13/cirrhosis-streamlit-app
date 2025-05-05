import os
import pandas as pd
import streamlit as st
from kaggle.api.kaggle_api_extended import KaggleApi

# Setup Kaggle API
with open("/tmp/kaggle.json", "w") as f:
    f.write(st.secrets["kaggle_json"])
os.environ['KAGGLE_CONFIG_DIR'] = "/tmp"

# Unduh dataset jika belum ada
def download_dataset():
    filename = "cirrhosis.csv"
    if not os.path.exists(filename):
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files("fedesoriano/cirrhosis-prediction-dataset", path=".", unzip=True)

download_dataset()

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("cirrhosis.csv")
    return df

df = load_data()

# Aplikasi Streamlit
st.title("Cirrhosis Prediction Dataset Viewer")

st.write("Dataset berisi informasi medis terkait pasien sirosis.")
st.dataframe(df.head())

# Filter by Gender
gender = st.selectbox("Filter berdasarkan Gender:", df["Gender"].dropna().unique())
filtered_df = df[df["Gender"] == gender]
st.write(f"Jumlah data untuk gender {gender}: {len(filtered_df)}")
st.dataframe(filtered_df)
