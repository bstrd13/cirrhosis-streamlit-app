import os
import streamlit as st
from kaggle.api.kaggle_api_extended import KaggleApi

# Ambil dari secrets
username = st.secrets["kaggle"]["username"]
key = st.secrets["kaggle"]["key"]

# Tulis ke ~/.kaggle/kaggle.json
kaggle_path = os.path.expanduser("~/.kaggle")
os.makedirs(kaggle_path, exist_ok=True)

with open(os.path.join(kaggle_path, "kaggle.json"), "w") as f:
    f.write(f"""{{
        "username": "{username}",
        "key": "{key}"
    }}""")

os.chmod(os.path.join(kaggle_path, "kaggle.json"), 0o600)

# Autentikasi
api = KaggleApi()
api.authenticate()
st.success("Berhasil terhubung ke Kaggle!")
