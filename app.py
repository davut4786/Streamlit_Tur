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

# Streamlit uygulamanızın geri kalan kodları
st.title("Hastalık Tahmin Uygulaması")

# Kullanıcıdan verileri alın
tur = st.selectbox("Tür", options=[("Kedi", 0), ("Köpek", 1)])
sistem = st.selectbox("Sistem", options=[("Bilinmiyor", 0), ("Boşaltım", 1), ("Deri", 2), ("Dolaşım", 3), ("Mix", 4), ("Sindirim", 5), ("Sinir", 6), ("Solunum", 7)])

# Diğer verileri almak için input alanları ekleyin
cBasebC = st.number_input("cBasebC", format="%.2f")
# Diğer input alanlarını buraya ekleyin...

if st.button("Tahmin Et"):
    # Model tahminini çalıştırın ve sonucu gösterin
    veriler = [tur, sistem, cBasebC]  # Gerekli tüm verileri ekleyin
    sonuc = model.predict([veriler])
    st.write(f"Tahmin Sonucu: {sonuc[0]}")
