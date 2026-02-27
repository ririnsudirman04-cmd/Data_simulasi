import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================
st.set_page_config(page_title="Dashboard Kepuasan Siswa", layout="wide")
st.title("📊 Dashboard Kepuasan Siswa (5 Responden)")
st.markdown("Visualisasi dan ringkasan data kepuasan berdasarkan 20 soal")

# ==========================================================
# LOAD DATA
# ==========================================================
df = pd.read_excel("data_5_siswa.xlsx")

# ==========================================================
# KPI UTAMA
# ==========================================================
st.subheader("📌 Ringkasan Kepuasan")
col1, col2 = st.columns(2)

with col1:
    st.metric("Jumlah Responden", df.shape[0])

with col2:
    st.metric("Jumlah Pertanyaan", df.shape[1])

# ==========================================================
# RATA-RATA PER SOAL
# ==========================================================
st.subheader("📈 Rata-rata Skor per Soal")
mean_scores = df.mean()

fig, ax = plt.subplots()
mean_scores.plot(kind="bar", ax=ax)
ax.set_ylabel("Skor Rata-rata")
ax.set_xlabel("Soal")
ax.set_title("Rata-rata Skor Kepuasan per Soal")
st.pyplot(fig)

# ==========================================================
# TABEL DATA
# ==========================================================
st.subheader("📋 Data Asli Responden")
st.dataframe(df)

# ==========================================================
# KESIMPULAN SINGKAT
# ==========================================================
st.subheader("📝 Kesimpulan")
st.write(
    "Dashboard ini menampilkan hasil survei kepuasan dari 5 siswa. "
    "Rata-rata skor dapat digunakan sebagai dasar evaluasi dan peningkatan kualitas layanan."
)
