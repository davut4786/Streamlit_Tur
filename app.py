import streamlit as st
import pickle
import os

# Model dosyasının mevcut olup olmadığını kontrol edin
model_path = 'hastalikturu_model.pkl'

if os.path.exists(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
else:
    st.error("Model dosyası bulunamadı! Lütfen 'hastalikturu_model.pkl' dosyasının var olduğundan emin olun.")

# Streamlit başlık
st.title("Hastalık Tahmin Uygulaması")

# Kullanıcıdan verileri al
tur = st.selectbox("Tür", options=["Kedi", "Köpek"])
sistem = st.selectbox("Sistem", options=["Bilinmiyor", "Boşaltım", "Deri", "Dolaşım", "Mix", "Sindirim", "Sinir", "Solunum"])

# Diğer veriler için sayısal giriş alanları (varsayılan boş, iki ondalık basamak)
cBasebC = st.number_input("cBasebC", format="%.2f", step=0.01, value=None)
cBaseEcfc = st.number_input("cBaseEcfc", format="%.2f", step=0.01, value=None)
HCO3Pc = st.number_input("HCO3Pc", format="%.2f", step=0.01, value=None)
p50c = st.number_input("p50c", format="%.2f", step=0.01, value=None)
cHCO3Pst = st.number_input("cHCO3Pst", format="%.2f", step=0.01, value=None)
cNa = st.number_input("cNa", format="%.2f", step=0.01, value=None)
FHHb = st.number_input("FHHb", format="%.2f", step=0.01, value=None)
sO2 = st.number_input("sO2", format="%.2f", step=0.01, value=None)
GRAN = st.number_input("GRAN", format="%.2f", step=0.01, value=None)
LYM = st.number_input("LYM", format="%.2f", step=0.01, value=None)
MON_A = st.number_input("MON_A", format="%.2f", step=0.01, value=None)
HCT = st.number_input("HCT", format="%.2f", step=0.01, value=None)
MCH = st.number_input("MCH", format="%.2f", step=0.01, value=None)
MCHC = st.number_input("MCHC", format="%.2f", step=0.01, value=None)

# Evet/Hayır seçenekleri için `selectbox` seçenekleri
abdominal_agri = st.selectbox("Abdominal Ağrı", options=["Hayır", "Evet"])
genel_durum = st.selectbox("Genel Durum", options=["Normal", "Hastalık"])
idar_problemi = st.selectbox("İdrar Problemi", options=["Hayır", "Evet"])
inkordinasyon = st.selectbox("İnkordinasyon", options=["Hayır", "Evet"])
ishal = st.selectbox("İshal", options=["Hayır", "Evet"])
istahsizlik = st.selectbox("İştahsızlık", options=["Hayır", "Evet"])
kanama = st.selectbox("Kanama", options=["Hayır", "Evet"])
kusma = st.selectbox("Kusma", options=["Hayır", "Evet"])
oksuruk = st.selectbox("Öksürük", options=["Hayır", "Evet"])

# Tahmin işlemi
if st.button("Tahmin Et"):
    # Model için giriş verilerini hazırlayın
    veriler = [
        1 if tur == "Köpek" else 0,
        sistem.index(sistem),
        cBasebC, cBaseEcfc, HCO3Pc, p50c, cHCO3Pst, cNa, FHHb, sO2, GRAN, LYM, MON_A, HCT, MCH, MCHC,
        1 if abdominal_agri == "Evet" else 0,
        1 if genel_durum == "Hastalık" else 0,
        1 if idar_problemi == "Evet" else 0,
        1 if inkordinasyon == "Evet" else 0,
        1 if ishal == "Evet" else 0,
        1 if istahsizlik == "Evet" else 0,
        1 if kanama == "Evet" else 0,
        1 if kusma == "Evet" else 0,
        1 if oksuruk == "Evet" else 0
    ]

    # Model tahmini ve sonuç gösterme
    try:
        sonuc = model.predict([veriler])
        st.write(f"Tahmin Sonucu: {sonuc[0]}")
    except Exception as e:
        st.error(f"Hata oluştu: {e}")
