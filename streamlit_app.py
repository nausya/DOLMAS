import yfinance as yf
import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Emas Terhadap Dollar Amerika',
    #page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data


# Mendapatkan data XAUUSD
# Fungsi untuk mengambil data harga emas berdasarkan tahun
def tampil(tahun_awal, tahun_akhir):
    data = yf.Ticker("GC=F")
    df = data.history(period="max")  # Mengambil seluruh data historis
    df = df[['Close']]
    
    # Filter data berdasarkan tahun yang dipilih
    df = df[(df.index.year >= tahun_awal) & (df.index.year <= tahun_akhir)]
    return df  

# Judul halaman
st.header('Grafik Harga Emas', divider='gray')

# Slider untuk memilih rentang tahun
tahun_awal, tahun_akhir = st.slider(
    'Pilih rentang tahun:',
    min_value=2000, max_value=2024,  # Rentang tahun yang tersedia
    value=(2015, 2024)  # Tahun default
)

# Memanggil fungsi tampil() dengan rentang tahun dari slider
df = tampil(tahun_awal, tahun_akhir)

# Menampilkan grafik menggunakan Streamlit
if not df.empty:
    st.line_chart(df)
else:
    st.write("Data tidak tersedia untuk rentang tahun yang dipilih.")
