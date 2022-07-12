import streamlit as st

#Mengimplementasikan Python Ke Sebuah Website
#Dengan Framework Streamlit
#By ZNainDEV

#github : https://www.github.com/veldanava

st.write("""
# Python Web Test
Rumus MTK Python via web
""")

alas = st.number_input("Masukan Alas Segitiga", 0)
tinggi = st.number_input("Masukan Tinggi Segitiga", 0)
hitung = st.button("Hitung Luas Segitiga")

if hitung:
    luas = 0.5 * alas * tinggi
    st.success(f"Luas Segitiga Adalah {luas}")