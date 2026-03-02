
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dashboard Kepuasan Lengkap",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Kepuasan Siswa - Versi Lengkap")
st.markdown("Dashboard Analisis Survei Kepuasan dengan Statistik & Visualisasi Lengkap")
st.divider()

uploaded_file = st.file_uploader(
    "📂 Upload File Excel Survei (.xlsx)",
    type=["xlsx"]
)

if uploaded_file is not None:

    df = pd.read_excel(uploaded_file)

    # ============================
    # STATISTIK DASAR
    # ============================
    jumlah_responden = df.shape[0]
    jumlah_pertanyaan = df.shape[1]
    rata_per_soal = df.mean()
    rata_total = df.values.mean()

    st.subheader("📌 Ringkasan Statistik")

    col1, col2, col3 = st.columns(3)
    col1.metric("Jumlah Responden", jumlah_responden)
    col2.metric("Jumlah Pertanyaan", jumlah_pertanyaan)
    col3.metric("Rata-rata Keseluruhan", round(rata_total, 2))

    # ============================
    # INTERPRETASI OTOMATIS
    # ============================
    if rata_total >= 4:
        kategori = "Sangat Puas"
    elif rata_total >= 3:
        kategori = "Puas"
    elif rata_total >= 2:
        kategori = "Cukup"
    else:
        kategori = "Kurang Puas"

    st.success(f"Tingkat Kepuasan: {kategori}")

    # ============================
    # SOAL TERBAIK & TERBURUK
    # ============================
    soal_tertinggi = rata_per_soal.idxmax()
    soal_terendah = rata_per_soal.idxmin()

    st.subheader("🔎 Analisis Soal")
    st.write(f"✅ Soal dengan skor tertinggi: **{soal_tertinggi}**")
    st.write(f"⚠ Soal dengan skor terendah: **{soal_terendah}**")

    # ============================
    # GRAFIK PER SOAL
    # ============================
    st.subheader("📊 Grafik Rata-rata per Soal")

    fig1, ax1 = plt.subplots()
    ax1.bar(rata_per_soal.index, rata_per_soal.values)
    ax1.set_ylabel("Rata-rata Skor")
    ax1.set_xlabel("Pertanyaan")
    ax1.set_title("Rata-rata Skor Tiap Soal")
    plt.xticks(rotation=45)

    st.pyplot(fig1)

    # ============================
    # GRAFIK RATA-RATA KESELURUHAN
    # ============================
    st.subheader("📈 Grafik Rata-rata Keseluruhan")

    fig2, ax2 = plt.subplots()
    ax2.bar(["Rata-rata Total"], [rata_total])
    ax2.set_ylabel("Nilai")
    ax2.set_title("Rata-rata Kepuasan Keseluruhan")

    st.pyplot(fig2)

    # ============================
    # DATA & DOWNLOAD
    # ============================
    st.subheader("📄 Data Responden")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Data (CSV)",
        data=csv,
        file_name="hasil_survei_kepuasan.csv",
        mime="text/csv"
    )

    # ============================
    # KESIMPULAN OTOMATIS
    # ============================
    st.subheader("📝 Kesimpulan Otomatis")

    st.write(f"""
    Berdasarkan hasil survei dari **{jumlah_responden} responden** 
    dengan total **{jumlah_pertanyaan} pertanyaan**, diperoleh rata-rata 
    keseluruhan sebesar **{round(rata_total,2)}** yang termasuk dalam kategori 
    **{kategori}**.

    Pertanyaan dengan skor tertinggi adalah **{soal_tertinggi}**, 
    sedangkan yang terendah adalah **{soal_terendah}**.

    Hasil ini dapat digunakan sebagai dasar evaluasi dan peningkatan kualitas layanan.
    """)

else:
    st.info("Silakan upload file Excel untuk menampilkan dashboard.")



# =============================
# ANALISIS REGRESI LINEAR
# =============================
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.subheader("📈 Analisis Regresi Linear (Rata-rata per Soal)")

# Menghitung rata-rata per soal
rata_per_soal = df.mean()

# X = nomor soal
X = np.arange(1, len(rata_per_soal) + 1).reshape(-1, 1)

# Y = rata-rata tiap soal
Y = rata_per_soal.values.reshape(-1, 1)

# Model regresi
model = LinearRegression()
model.fit(X, Y)

a = model.intercept_[0]
b = model.coef_[0][0]
r2 = model.score(X, Y)

# Menampilkan persamaan
st.write("### Persamaan Regresi")
st.latex(f"Y = {a:.3f} + {b:.3f}X")
st.write(f"Koefisien Determinasi (R²) = {r2:.3f}")

# Grafik regresi
Y_pred = model.predict(X)

fig, ax = plt.subplots()
ax.scatter(X, Y)
ax.plot(X, Y_pred)
ax.set_xlabel("Nomor Soal")
ax.set_ylabel("Rata-rata Skor")
ax.set_title("Regresi Linear Rata-rata per Soal")

st.pyplot(fig)

# Interpretasi otomatis
if b > 0:
    st.success("Terdapat tren peningkatan skor seiring bertambahnya nomor soal.")
elif b < 0:
    st.warning("Terdapat tren penurunan skor seiring bertambahnya nomor soal.")
else:
    st.info("Tidak terdapat hubungan antara nomor soal dan rata-rata skor.")
