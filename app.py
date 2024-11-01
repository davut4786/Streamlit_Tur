import streamlit as st
import pickle
import os
import numpy as np  # NumPy eklendi

# Model dosyasının mevcut olup olmadığını kontrol edin
model_path = 'hastalikturu_model.pkl'

if os.path.exists(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
else:
    st.error("Model dosyası bulunamadı! Lütfen 'hastalikturu_model.pkl' dosyasının var olduğundan emin olun.")

# Streamlit uygulamanızın arayüzü
st.title("Hastalık Tahmin Uygulaması")

# Kullanıcıdan verileri alın
tur = st.selectbox("Tür", options=[("Kedi", 0), ("Köpek", 1)])[1]
sistem = st.selectbox("Sistem", options=[
    ("Bilinmiyor", 0), ("Boşaltım", 1), ("Deri", 2), ("Dolaşım", 3),
    ("Mix", 4), ("Sindirim", 5), ("Sinir", 6), ("Solunum", 7)
])[1]

# Sayısal değer girişleri
cBasebC = st.number_input("cBasebC", format="%.2f")
cBaseEcfc = st.number_input("cBaseEcfc", format="%.2f")
HCO3Pc = st.number_input("HCO3Pc", format="%.2f")
p50c = st.number_input("p50c", format="%.2f")
cHCO3Pst = st.number_input("cHCO3Pst", format="%.2f")
cNa = st.number_input("cNa", format="%.2f")
FHHb = st.number_input("FHHb", format="%.2f")
sO2 = st.number_input("sO2", format="%.2f")
GRAN = st.number_input("GRAN", format="%.2f")
LYM = st.number_input("LYM", format="%.2f")
MON_A = st.number_input("MON_A", format="%.2f")
HCT = st.number_input("HCT", format="%.2f")
MCH = st.number_input("MCH", format="%.2f")
MCHC = st.number_input("MCHC", format="%.2f")

# Kategorik değer girişleri
abdominal_agri = st.selectbox("Abdominal Ağrı", options=[("Hayır", 0), ("Evet", 1)])[1]
genel_durum = st.selectbox("Genel Durum", options=[("Normal", 0), ("Hastalık", 1)])[1]
idar_problemi = st.selectbox("İdrar Problemi", options=[("Hayır", 0), ("Evet", 1)])[1]
inkordinasyon = st.selectbox("İnkordinasyon", options=[("Hayır", 0), ("Evet", 1)])[1]
ishal = st.selectbox("İshal", options=[("Hayır", 0), ("Evet", 1)])[1]
istahsizlik = st.selectbox("İştahsızlık", options=[("Hayır", 0), ("Evet", 1)])[1]
kanama = st.selectbox("Kanama", options=[("Hayır", 0), ("Evet", 1)])[1]
kusma = st.selectbox("Kusma", options=[("Hayır", 0), ("Evet", 1)])[1]
oksuruk = st.selectbox("Öksürük", options=[("Hayır", 0), ("Evet", 1)])[1]

# Tahmin butonu
if st.button("Tahmin Et"):
    veriler = np.array([  # NumPy array ile veriler düzene kondu
        tur, sistem, cBasebC, cBaseEcfc, HCO3Pc, p50c, cHCO3Pst, cNa, FHHb, sO2, GRAN,
        LYM, MON_A, HCT, MCH, MCHC, abdominal_agri, genel_durum, idar_problemi, inkordinasyon,
        ishal, istahsizlik, kanama, kusma, oksuruk
    ]).reshape(1, -1)  # Modelin beklediği şekle uygun hale getirildi

    # Model tahminini yapın ve sonucu gösterin
    try:
        sonuc = model.predict(veriler)
        st.write(f"Tahmin Sonucu: {sonuc[0]}")
    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")
