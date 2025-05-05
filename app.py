import os
import streamlit as st
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

# Set environment variables for Kaggle authentication
os.environ["KAGGLE_USERNAME"] = st.secrets["kaggle"]["username"]
os.environ["KAGGLE_KEY"] = st.secrets["kaggle"]["key"]

# Authenticate with Kaggle API
api = KaggleApi()
api.authenticate()

# Function to download dataset
@st.cache_data
def download_dataset():
    dataset_name = "fedesoriano/cirrhosis-prediction-dataset"
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)
    api.dataset_download_files(dataset_name, path=output_dir, unzip=True)
    return os.path.join(output_dir, "cirrhosis.csv")

# Download and load dataset
csv_path = download_dataset()
df = pd.read_csv(csv_path)

# Display the dataset
st.title("🩺 Cirrhosis Prediction Dataset Viewer")
st.dataframe(df.head())

