import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Header dan deskripsi
st.markdown("""
# 🩺 Prediksi Sirosis Hati
Aplikasi untuk memprediksi kemungkinan sirosis hati berdasarkan data medis. 
Silakan lihat dataset dan jelajahi hasil prediksi di bawah ini.
""")

# Sidebar untuk input
st.sidebar.header("Pengaturan Prediksi")
age = st.sidebar.slider("Pilih usia:", 20, 100, 30)
gender = st.sidebar.radio("Jenis Kelamin:", ("Laki-laki", "Perempuan"))

# Membaca dan menampilkan dataset
df = pd.read_csv("data/cirrhosis.csv")

# Menampilkan dataframe
st.subheader("Dataset Sirosis Hati")
st.dataframe(df, width=700)

# Grafik distribusi usia
fig, ax = plt.subplots()
ax.hist(df["age"], bins=10, color="skyblue")
ax.set_title("Distribusi Umur")
st.pyplot(fig)

# Kolom untuk tampilan terpisah
col1, col2 = st.columns(2)

with col1:
    st.header("Informasi Tambahan")
    st.write("Dataset ini berisi data medis terkait dengan sirosis hati.")
    
with col2:
    st.header("Grafik Lainnya")
    st.write("Di sini, Anda bisa melihat visualisasi lainnya.")

# Menambahkan grafik interaktif
fig = px.histogram(df, x="Age", title="Distribusi Usia")
st.plotly_chart(fig)

# Footer
st.markdown("""
---
Made with ❤️ by [ahmad mulyana](https://github.com/bstrd13)
""")
