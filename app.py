import streamlit as st
import pickle
import os

# Model dosyasının mevcut olup olmadığını kontrol edin
model_path = 'hastalikturu_model.pkl'

if os.path.exists(model_path):
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
    except Exception as e:
        st.error(f"Model dosyası yüklenirken hata oluştu: {e}")
else:
    st.error("Model dosyası bulunamadı! Lütfen 'hastalikturu_model.pkl' dosyasının var olduğundan emin olun.")

# Streamlit uygulamanızın geri kalan kodları
st.title("Hastalık Tahmin Uygulaması")

# Kullanıcıdan verileri alın
tur = st.selectbox("Tür", options=["Kedi", "Köpek"])
sistem = st.selectbox("Sistem", options=["Bilinmiyor", "Boşaltım", "Deri", "Dolaşım", "Mix", "Sindirim", "Sinir", "Solunum"])

# Diğer seçilen özellikler için selectboxlar ekleyin
abdominal_agri = st.selectbox("Abdominal Ağrı", options=["Hayır", "Evet"])
genel_durum = st.selectbox("Genel Durum", options=["Kötü", "İyi"])
idar_problemi = st.selectbox("İdrar Problemi", options=["Hayır", "Evet"])
inkordinasyon = st.selectbox("İnkordinasyon", options=["Hayır", "Evet"])
ishal = st.selectbox("İshal", options=["Hayır", "Evet"])
istahsizlik = st.selectbox("İstahsızlık", options=["Hayır", "Evet"])
kanama = st.selectbox("Kanama", options=["Hayır", "Evet"])
kusma = st.selectbox("Kusma", options=["Hayır", "Evet"])
oksuruk = st.selectbox("Öksürük", options=["Hayır", "Evet"])

# Sayısal değerler için input alanları
cols = st.columns(5)  # 5 sütun oluştur
cBasebC = cols[0].number_input("cBasebC", format="%.2f", value=0.0, step=0.01)
cBaseEcfc = cols[1].number_input("cBaseEcfc", format="%.2f", value=0.0, step=0.01)
HCO3Pc = cols[2].number_input("HCO3Pc", format="%.2f", value=0.0, step=0.01)
p50c = cols[3].number_input("p50c", format="%.2f", value=0.0, step=0.01)
cHCO3Pst = cols[4].number_input("cHCO3Pst", format="%.2f", value=0.0, step=0.01)

# Diğer sayısal değerler için ek sütunlar oluştur
cols2 = st.columns(5)
cNa = cols2[0].number_input("cNa", format="%.2f", value=0.0, step=0.01)
FHHb = cols2[1].number_input("FHHb", format="%.2f", value=0.0, step=0.01)
sO2 = cols2[2].number_input("sO2", format="%.2f", value=0.0, step=0.01)
GRAN = cols2[3].number_input("GRAN", format="%.2f", value=0.0, step=0.01)
LYM = cols2[4].number_input("LYM", format="%.2f", value=0.0, step=0.01)

# Tahmin butonu
if st.button("Tahmin Et"):
    # Model tahminini çalıştırın ve sonucu gösterin
    veriler = [
        tur,
        sistem,
        abdominal_agri,
        genel_durum,
        idar_problemi,
        inkordinasyon,
        ishal,
        istahsızlık,
        kanama,
        kusma,
        oksuruk,
        cBasebC,
        cBaseEcfc,
        HCO3Pc,
        p50c,
        cHCO3Pst,
        cNa,
        FHHb,
        sO2,
        GRAN,
        LYM
    ]  # Gerekli tüm verileri ekleyin
    sonuc = model.predict([veriler])
    st.write(f"Tahmin Sonucu: {sonuc[0]}")

# CSS ile kutuların etrafındaki kenarlıkları mavi yapalım
st.markdown(
    """
    <style>
    .stNumberInput {
        border: 2px solid blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)
