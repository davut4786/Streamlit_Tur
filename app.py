import streamlit as st
import anvil.server

# Anvil sunucusuna bağlanma
anvil.server.connect("server_KORPUEPN5NQLQLYFM2J65VBN-47GGCVO2CJ7A57PR")  # Anvil sunucusu anahtarınızı buraya ekleyin

# Başlık ve açıklama
st.title("Hastalık Türü Tahmin Uygulaması")
st.write("Lütfen aşağıdaki alanları doldurarak tahmin yapın.")

# Dropdown seçenekleri
tur_dict = {"Kedi": 0, "Köpek": 1}
sistem_dict = {
    "Bilinmiyor": 0, "Boşaltım": 1, "Deri": 2, "Dolaşım": 3,
    "Mix": 4, "Sindirim": 5, "Sinir": 6, "Solunum": 7
}
binary_options = {"Hayır": 0, "Evet": 1}
genel_durum_options = {"Normal": 0, "Hastalık": 1}

# Kullanıcıdan giriş al
tur = st.selectbox("Tür", list(tur_dict.keys()))
sistem = st.selectbox("Sistem", list(sistem_dict.keys()))

# Numerik alanlar için giriş al
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

# Diğer dropdown seçimleri
abdominal_agri = st.selectbox("Abdominal Ağrı", list(binary_options.keys()))
genel_durum = st.selectbox("Genel Durum", list(genel_durum_options.keys()))
idar_problemi = st.selectbox("İdar Problemi", list(binary_options.keys()))
inkordinasyon = st.selectbox("İnkordinasyon", list(binary_options.keys()))
ishal = st.selectbox("İshal", list(binary_options.keys()))
istahsizlik = st.selectbox("İştahsızlık", list(binary_options.keys()))
kanama = st.selectbox("Kanama", list(binary_options.keys()))
kusma = st.selectbox("Kusma", list(binary_options.keys()))
oksuruk = st.selectbox("Öksürük", list(binary_options.keys()))

# Tahmin butonu
if st.button("Tahmin Et"):
    # Kullanıcı verilerini liste halinde düzenleme
    veriler = [
        tur_dict[tur], sistem_dict[sistem], cBasebC, cBaseEcfc, HCO3Pc, p50c, 
        cHCO3Pst, cNa, FHHb, sO2, GRAN, LYM, MON_A, HCT, MCH, MCHC,
        binary_options[abdominal_agri], genel_durum_options[genel_durum], 
        binary_options[idar_problemi], binary_options[inkordinasyon], 
        binary_options[ishal], binary_options[istahsizlik], 
        binary_options[kanama], binary_options[kusma], binary_options[oksuruk]
    ]
    
    # Model ile tahmin yapma
    sonuc = anvil.server.call('model_tahmin', veriler)

    # Sonucu göster
    st.write(f"Tahmin Sonucu: {sonuc}")
