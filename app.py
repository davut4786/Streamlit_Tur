import streamlit as st
import pickle

# Modeli yüklemek için gereken dosya yolu (modelinizi GitHub’a yüklediğinizi varsayarak)
model_path = 'hastalikturu_model.pkl'

# Modeli yükleyin
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Streamlit başlık
st.title("Hastalık Tahmin Uygulaması")

# Kullanıcı girişleri için alanlar oluştur
tur = st.selectbox("Tür", [("Kedi", 0), ("Köpek", 1)])
sistem = st.selectbox("Sistem", [
    ("Bilinmiyor", 0), ("Boşaltım", 1), ("Deri", 2), 
    ("Dolaşım", 3), ("Mix", 4), ("Sindirim", 5), 
    ("Sinir", 6), ("Solunum", 7)
])

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

abdominal_agri = st.selectbox("Abdominal Ağrı", [("Hayır", 0), ("Evet", 1)])
genel_durum = st.selectbox("Genel Durum", [("Normal", 0), ("Hastalık", 1)])
idar_problemi = st.selectbox("İdar Problemi", [("Hayır", 0), ("Evet", 1)])
inkordinasyon = st.selectbox("İnkordinasyon", [("Hayır", 0), ("Evet", 1)])
ishal = st.selectbox("İshal", [("Hayır", 0), ("Evet", 1)])
istahsizlik = st.selectbox("İştahsızlık", [("Hayır", 0), ("Evet", 1)])
kanama = st.selectbox("Kanama", [("Hayır", 0), ("Evet", 1)])
kusma = st.selectbox("Kusma", [("Hayır", 0), ("Evet", 1)])
oksuruk = st.selectbox("Öksürük", [("Hayır", 0), ("Evet", 1)])

# Tahmin butonu
if st.button("Tahmin Et"):
    # Model tahmini yapmak için verileri uygun formata getirin
    veriler = [
        tur[1], sistem[1], cBasebC, cBaseEcfc, HCO3Pc, p50c, cHCO3Pst, 
        cNa, FHHb, sO2, GRAN, LYM, MON_A, HCT, MCH, MCHC, 
        abdominal_agri[1], genel_durum[1], idar_problemi[1], inkordinasyon[1], 
        ishal[1], istahsizlik[1], kanama[1], kusma[1], oksuruk[1]
    ]

    # Model tahminini al
    tahmin = model.predict([veriler])[0]

    # Tahmin sonucunu göster
    st.write(f"Tahmin Sonucu: {tahmin}")

