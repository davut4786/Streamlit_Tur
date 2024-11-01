import streamlit as st
import pickle
import os
import numpy as np

# Model dosyasının mevcut olup olmadığını kontrol edin
model_path = 'hastalikturu_model.pkl'

if os.path.exists(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
else:
    st.error("Model dosyası bulunamadı! Lütfen 'hastalikturu_model.pkl' dosyasının var olduğundan emin olun.")

# Streamlit uygulamanızın geri kalan kodları
st.title("Hastalık Tahmin Uygulaması")

# Kullanıcıdan verileri almak için kutuları yan yana düzenle
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    tur = st.selectbox("Tür", options=["Kedi", "Köpek"], format_func=lambda x: "Kedi" if x == "Kedi" else "Köpek")

with col2:
    sistem = st.selectbox("Sistem", options=["Bilinmiyor", "Boşaltım", "Deri", "Dolaşım", "Mix", "Sindirim", "Sinir", "Solunum"],
                           format_func=lambda x: x)

with col3:
    cBasebC = st.number_input("cBasebC", format="%.2f", value=0.0, step=0.01, min_value=0.0)

with col4:
    cBaseEcfc = st.number_input("cBaseEcfc", format="%.2f", value=0.0, step=0.01, min_value=0.0)

with col5:
    HCO3Pc = st.number_input("HCO3Pc", format="%.2f", value=0.0, step=0.01, min_value=0.0)

# İkinci satır için başka giriş alanları ekle
col6, col7, col8, col9, col10 = st.columns(5)

with col6:
    p50c = st.number_input("p50c", format="%.2f", value=0.0, step=0.01, min_value=0.0)

with col7:
    cHCO3Pst = st.number_input("cHCO3Pst", format="%.2f", value=0.0, step=0.01, min_value=0.0)

with col8:
    cNa = st.number_input("cNa", format="%.2f", value=0.0, step=0.01, min_value=0.0)

with col9:
    FHHb = st.number_input("FHHb", format="%.2f", value=0.0, step=0.01, min_value=0.0)

with col10:
    sO2 = st.number_input("sO2", format="%.2f", value=0.0, step=0.01, min_value=0.0)

# Üçüncü satır için giriş alanları
col11, col12, col13, col14, col15 = st.columns(5)

with col11:
    GRAN = st.number_input("GRAN", format="%.2f", value=0.0, step=0.01, min_value=0.0)

with col12:
    LYM = st.number_input("LYM", format="%.2f", value=0.0, step=0.01, min_value=0.0)

with col13:
    MON_A = st.number_input("MON_A", format="%.2f", value=0.0, step=0.01, min_value=0.0)

with col14:
    HCT = st.number_input("HCT", format="%.2f", value=0.0, step=0.01, min_value=0.0)

with col15:
    MCH = st.number_input("MCH", format="%.2f", value=0.0, step=0.01, min_value=0.0)

# Dördüncü satır için giriş alanları
col16, col17, col18, col19, col20 = st.columns(5)

with col16:
    MCHC = st.number_input("MCHC", format="%.2f", value=0.0, step=0.01, min_value=0.0)

with col17:
    abdominal_agri = st.selectbox("Abdominal Ağrı", options=["Hayır", "Evet"])

with col18:
    genel_durum = st.selectbox("Genel Durum", options=["Hayır", "Evet"])

with col19:
    idar_problemi = st.selectbox("İdrar Problemi", options=["Hayır", "Evet"])

with col20:
    inkordinasyon = st.selectbox("İnkordinasyon", options=["Hayır", "Evet"])

# Beşinci satır için giriş alanları
col21, col22, col23, col24, col25 = st.columns(5)

with col21:
    ishal = st.selectbox("İshal", options=["Hayır", "Evet"])

with col22:
    istahsızlık = st.selectbox("İstahsızlık", options=["Hayır", "Evet"])

with col23:
    kanama = st.selectbox("Kanama", options=["Hayır", "Evet"])

with col24:
    kusma = st.selectbox("Kusma", options=["Hayır", "Evet"])

with col25:
    oksuruk = st.selectbox("Öksürük", options=["Hayır", "Evet"])

# Butonu daha aşağıda konumlandırma
st.markdown("<br><br>", unsafe_allow_html=True)  # Boşluk eklemek için

# Tahmin et butonu
if st.button("Tahmin Et", key="tahmin_et", style="background-color: blue; color: white;"):
    # Model tahminini çalıştırın ve sonucu gösterin
    veriler = [
        tur, sistem,
        float(cBasebC), float(cBaseEcfc), float(HCO3Pc), float(p50c), float(cHCO3Pst), float(cNa),
        float(FHHb), float(sO2), float(GRAN), float(LYM), float(MON_A),
        float(HCT), float(MCH), float(MCHC), abdominal_agri, genel_durum,
        idar_problemi, inkordinasyon, ishal, istahsızlık, kanama, kusma, oksuruk
    ]

    # Modelin beklediği formatı sağlamak için numpy dizisine çeviriyoruz
    veriler = np.array(veriler).reshape(1, -1)  # Girdi dizisini 2D hale getiriyoruz

    sonuc = model.predict(veriler)
    st.write(f"Tahmin Sonucu: {sonuc[0]}")
