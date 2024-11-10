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
def tampil():
    data = yf.Ticker("GC=F")
    df = data.history(period="5d")  # Mengambil data selama 5 hari terakhir
    df = df['Close']
    return df  

st.header('Grafik', divider='gray')

# Memanggil fungsi tampil untuk mendapatkan data
df = tampil()

# Menampilkan grafik menggunakan Streamlit
st.line_chart(df)
