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

# Fungsi untuk mengambil data harga emas berdasarkan tahun dan kolom yang dipilih
import yfinance as yf
import streamlit as st
import pandas as pd

# Fungsi untuk mengambil data harga emas berdasarkan tahun dan kolom yang dipilih
def tampil(tahun_awal, tahun_akhir, kolom_terpilih):
    data = yf.Ticker("GC=F")
    df = data.history(period="max")  # Mengambil seluruh data historis
    
    # Filter data berdasarkan tahun yang dipilih
    df = df[(df.index.year >= tahun_awal) & (df.index.year <= tahun_akhir)]
    
    # Memastikan kolom yang dipilih tersedia di data
    df = df[kolom_terpilih]  # Mengembalikan hanya kolom yang dipilih
    return df

# Judul halaman
st.header('Grafik Harga Emas', divider='gray')

# Slider untuk memilih rentang tahun
tahun_awal, tahun_akhir = st.slider(
    'Pilih rentang tahun:',
    min_value=2000, max_value=2023,  # Rentang tahun yang tersedia
    value=(2015, 2023)  # Tahun default
)

# Multiselect untuk memilih beberapa kolom data
kolom_terpilih = st.multiselect(
    'Pilih jenis data yang ingin ditampilkan:',
    options=['Open', 'High', 'Low', 'Close'],
    default=['Close']  # Nilai default
)

# Memanggil fungsi tampil() dengan rentang tahun dan kolom yang dipilih
if kolom_terpilih:
    df = tampil(tahun_awal, tahun_akhir, kolom_terpilih)
    
    # Menampilkan grafik menggunakan Streamlit jika data tersedia
    if not df.empty:
        st.line_chart(df)
    else:
        st.write("Data tidak tersedia untuk rentang tahun yang dipilih.")
else:
    st.write("Silakan pilih setidaknya satu kolom data untuk ditampilkan.")


