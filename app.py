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

st.title("Hastalık Tahmin Uygulaması")

# Kullanıcıdan verileri alın
tur = st.selectbox("Tür", options=["Kedi", "Köpek"], index=0)
sistem = st.selectbox("Sistem", options=["Bilinmiyor", "Boşaltım", "Deri", "Dolaşım", "Mix", "Sindirim", "Sinir", "Solunum"], index=0)

# Sayısal değerler için input alanları
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    cBasebC = st.number_input("cBasebC", format="%.2f", step=0.01, min_value=0.0, value=0.0)
with col2:
    cBaseEcfc = st.number_input("cBaseEcfc", format="%.2f", step=0.01, min_value=0.0, value=0.0)
with col3:
    HCO3Pc = st.number_input("HCO3Pc", format="%.2f", step=0.01, min_value=0.0, value=0.0)
with col4:
    p50c = st.number_input("p50c", format="%.2f", step=0.01, min_value=0.0, value=0.0)
with col5:
    cHCO3Pst = st.number_input("cHCO3Pst", format="%.2f", step=0.01, min_value=0.0, value=0.0)

# Diğer sayısal değişkenler için input alanları
cNa = st.number_input("cNa", format="%.2f", step=0.01, min_value=0.0, value=0.0)
FHHb = st.number_input("FHHb", format="%.2f", step=0.01, min_value=0.0, value=0.0)
sO2 = st.number_input("sO2", format="%.2f", step=0.01, min_value=0.0, value=0.0)
GRAN = st.number_input("GRAN", format="%.2f", step=0.01, min_value=0.0, value=0.0)
LYM = st.number_input("LYM", format="%.2f", step=0.01, min_value=0.0, value=0.0)
MON_A = st.number_input("MON_A", format="%.2f", step=0.01, min_value=0.0, value=0.0)
HCT = st.number_input("HCT", format="%.2f", step=0.01, min_value=0.0, value=0.0)
MCH = st.number_input("MCH", format="%.2f", step=0.01, min_value=0.0, value=0.0)
MCHC = st.number_input("MCHC", format="%.2f", step=0.01, min_value=0.0, value=0.0)

# Kategorik değişkenler için selectbox
abdominal_agri = st.selectbox("Abdominal Ağrı", options=["Hayır", "Evet"])
genel_durum = st.selectbox("Genel Durum", options=["Hayır", "Evet"])
idar_problemi = st.selectbox("İdar Problemi", options=["Hayır", "Evet"])
inkordinasyon = st.selectbox("İnkoordinasyon", options=["Hayır", "Evet"])
ishal = st.selectbox("İshal", options=["Hayır", "Evet"])
istahsizlik = st.selectbox("İstahsızlık", options=["Hayır", "Evet"])
kanama = st.selectbox("Kanama", options=["Hayır", "Evet"])
kusma = st.selectbox("Kusma", options=["Hayır", "Evet"])
oksuruk = st.selectbox("Öksürük", options=["Hayır", "Evet"])

# Tahmin et butonu
if st.button("Tahmin Et", key="tahmin_et"):
    veriler = [
        tur,
        sistem,
        cBasebC,
        cBaseEcfc,
        HCO3Pc,
        p50c,
        cHCO3Pst,
        cNa,
        FHHb,
        sO2,
        GRAN,
        LYM,
        MON_A,
        HCT,
        MCH,
        MCHC,
        abdominal_agri,
        genel_durum,
        idar_problemi,
        inkordinasyon,
        ishal,
        istahsizlik,
        kanama,
        kusma,
        oksuruk,
    ]
    
    # Model tahminini çalıştırın ve sonucu gösterin
    sonuc = model.predict([veriler])
    st.write(f"Tahmin Sonucu: {sonuc[0]}")

# CSS ile görünümü özelleştirme
st.markdown(
    """
    <style>
    .stButton {
        background-color: blue;
        color: white;
        margin-top: 20px;
    }
    .stNumberInput {
        border: 2px solid blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)
