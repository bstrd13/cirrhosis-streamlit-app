import os
import json
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from kaggle.api.kaggle_api_extended import KaggleApi

# Ambil credentials dari secrets
kaggle_token = {
    "username": st.secrets["kaggle"]["username"],
    "key": st.secrets["kaggle"]["key"]
}

# Tulis ke file kaggle.json
os.makedirs(os.path.expanduser("~/.kaggle"), exist_ok=True)
with open(os.path.expanduser("~/.kaggle/kaggle.json"), "w") as f:
    json.dump(kaggle_token, f)
os.chmod(os.path.expanduser("~/.kaggle/kaggle.json"), 0o600)

# Autentikasi ke Kaggle
api = KaggleApi()
api.authenticate()

# Download dataset
@st.cache_data
def download_dataset():
    dataset_name = "fedesoriano/cirrhosis-prediction-dataset"
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)
    api.dataset_download_files(dataset_name, path=output_dir, unzip=True)
    return os.path.join(output_dir, "cirrhosis.csv")

# Load dataset
csv_path = download_dataset()
df = pd.read_csv(csv_path)

# Tampilkan
st.title("🩺 Cirrhosis Prediction Dataset Viewer")
st.dataframe(df.head())

