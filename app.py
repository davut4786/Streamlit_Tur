import streamlit as st
import pickle
import os

# Model dosyasının mevcut olup olmadığını kontrol edin
model_path = 'hastalikturu_model.pkl'

if os.path.exists(model_path):
    if os.path.getsize(model_path) > 0:  # Check if the file is not empty
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
    else:
        st.error("Model dosyası boş! Lütfen geçerli bir model dosyası yükleyin.")
else:
    st.error("Model dosyası bulunamadı! Lütfen 'hastalikturu_model.pkl' dosyasının var olduğundan emin olun.")

# Streamlit başlık
st.title("Hastalık Durumu Tahmin Uygulaması")

# Kullanıcıdan verileri al
tur = st.selectbox("Tür", options=["Seç", "Kedi", "Köpek"])
sistem = st.selectbox("Sistem", options=["Seç", "Bilinmiyor", "Boşaltım", "Deri", "Dolaşım", "Mix (en az 2 sistem)", "Sindirim", "Sinir", "Solunum"])

# Diğer veriler için sayısal giriş alanları (varsayılan boş, iki ondalık basamak)
cBasebC = st.number_input("cBasebC")
cBaseEcfc = st.number_input("cBaseEcfc")
HCO3Pc = st.number_input("HCO3Pc")
p50c = st.number_input("p50c")
cHCO3Pst = st.number_input("cHCO3Pst")
cNa = st.number_input("cNa")
FHHb = st.number_input("FHHb")
sO2 = st.number_input("sO2", format="%.2f", step=0.01, value=None, key="sO2", min_value=0.0)
GRAN = st.number_input("GRAN", format="%.2f", step=0.01, value=None, key="GRAN", min_value=0.0)
LYM = st.number_input("LYM", format="%.2f", step=0.01, value=None, key="LYM", min_value=0.0)
MON_A = st.number_input("MON_A", format="%.2f", step=0.01, value=None, key="MON_A", min_value=0.0)
HCT = st.number_input("HCT", format="%.2f", step=0.01, value=None, key="HCT", min_value=0.0)
MCH = st.number_input("MCH", format="%.2f", step=0.01, value=None, key="MCH", min_value=0.0)
MCHC = st.number_input("MCHC", format="%.2f", step=0.01, value=None, key="MCHC", min_value=0.0)

# Evet/Hayır seçenekleri için `selectbox` seçenekleri
abdominal_agri = st.selectbox("Abdominal Ağrı", options=["Yok", "Var"])
genel_durum = st.selectbox("Genel Durum", options=["İyi", "Kötü"])
idar_problemi = st.selectbox("İdrar Problemi", options=["Yok", "Var"])
inkordinasyon = st.selectbox("İnkordinasyon", options=["Yok", "Var"])
ishal = st.selectbox("İshal", options=["Yok", "Var"])
istahsizlik = st.selectbox("İştahsızlık", options=["Yok", "Var"])
kanama = st.selectbox("Kanama", options=["Yok", "Var"])
kusma = st.selectbox("Kusma", options=["Hayır", "Evet"])
oksuruk = st.selectbox("Öksürük", options=["Yok", "Var"])

# Tahmin işlemi
if st.button("Tahmin Et"):
    # Giriş verilerini kontrol et
    empty_fields = []
    input_keys = {
        "cBasebC": cBasebC,
        "cBaseEcfc": cBaseEcfc,
        "HCO3Pc": HCO3Pc,
        "p50c": p50c,
        "cHCO3Pst": cHCO3Pst,
        "cNa": cNa,
        "FHHb": FHHb,
        "sO2": sO2,
        "GRAN": GRAN,
        "LYM": LYM,
        "MON_A": MON_A,
        "HCT": HCT,
        "MCH": MCH,
        "MCHC": MCHC,
    }

    # "Tür" ve "Sistem" için varsayılan kontrol
    if tur == "Seçin":
        empty_fields.append("Tür")
    if sistem == "Seçin":
        empty_fields.append("Sistem")

    for key, value in input_keys.items():
        if value is None:
            empty_fields.append(f"{key} (sayısal değer)")

    if empty_fields:
        # Hata mesajı oluşturma
        error_messages = []
        for field in empty_fields:
            error_messages.append(f"Lütfen {field} giriniz.")
        
        # Hata mesajlarını göster
        st.error(" ".join(error_messages))

        # Boş alanları vurgulama
        for field in empty_fields:
            st.markdown(f"<style>#{field} {{ border: 2px solid red; }}</style>", unsafe_allow_html=True)
            # İmleci boş olan alana odaklamak için JavaScript ekleyin
            st.markdown(f"<script>document.getElementById('{field}').focus();</script>", unsafe_allow_html=True)
    else:
        # Model için giriş verilerini hazırlayın
        veriler = [
            1 if tur == "Köpek" else 0,
            sistem.index(sistem) - 1,  # "Seçin" durumu için bir ayarlama
            cBasebC, cBaseEcfc, HCO3Pc, p50c, cHCO3Pst, cNa, FHHb, sO2, GRAN, LYM, MON_A, HCT, MCH, MCHC,
            1 if abdominal_agri == "Var" else 0,
            1 if genel_durum == "Kötü" else 0,
            1 if idar_problemi == "Var" else 0,
            1 if inkordinasyon == "Var" else 0,
            1 if ishal == "Var" else 0,
            1 if istahsizlik == "Var" else 0,
            1 if kanama == "Var" else 0,
            1 if kusma == "Var" else 0,
            1 if oksuruk == "Var" else 0
        ]

        # Model tahmini ve sonuç gösterme
        try:
            sonuc = model.predict([veriler])
            st.write(f"Tahmin Sonucu: {sonuc[0]}")
        except Exception as e:
            st.error(f"Hata oluştu: {e}")
