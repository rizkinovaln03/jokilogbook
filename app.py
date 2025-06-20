import streamlit as st
from main_runner import isi_semua_logbook

st.set_page_config(page_title="Joki Logbook Koass", page_icon="🩺")
st.title("🩺 JOKI LOGBOOK KOASS OTOMATIS")

username = st.text_input("👤 Username")
password = st.text_input("🔒 Password", type="password")
id_stase = st.text_input("🏥 ID Stase (Contoh: M096)")
tanggal = st.date_input("📅 Tanggal").strftime('%Y-%m-%d')

if st.button("🚀 Jalankan Semua Logbook"):
    with st.spinner("⏳ Menjalankan semua proses..."):
        try:
            isi_semua_logbook(username, password, id_stase, tanggal)
            st.success("✅ Semua logbook berhasil diisi dan di-approve!")
        except Exception as e:
            st.error(f"❌ Gagal: {e}")