import streamlit as st
import os
from penyakit_logbook import isi_logbook_penyakit
from ketrampilan_logbook import isi_logbook_ketrampilan
from eval_akhir import isi_eval_akhir
from approve_penyakit import approve_logbook_penyakit
from approve_ketrampilan import approve_logbook_ketrampilan

OUTPUT_FILE = "logbook_selesai.txt"  # ganti dengan PDF nanti

def jalankan_semua(username, password, id_stase, tanggal):
    isi_logbook_penyakit(username, password, id_stase, tanggal)
    isi_logbook_ketrampilan(username, password, id_stase, tanggal)
    isi_eval_akhir(username, password, id_stase)
    approve_logbook_penyakit(username, password, id_stase, tanggal)
    approve_logbook_ketrampilan(username, password, id_stase, tanggal)

    # Buat file dummy sebagai hasil
    with open(OUTPUT_FILE, "w") as f:
        f.write(f"Logbook untuk {username} - {id_stase} selesai pada {tanggal}\n")
        f.write("Sudah diisi dan di-approve otomatis.\n")

# Streamlit UI
st.title("🩺 Sistem Otomatis Pengisian Logbook Koass")

with st.form("logbook_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    id_stase = st.text_input("ID Stase (contoh: M096)")
    tanggal = st.date_input("Tanggal").strftime('%Y-%m-%d')
    submitted = st.form_submit_button("🚀 Jalankan dan Unduh File")

if submitted:
    try:
        jalankan_semua(username, password, id_stase, tanggal)
        with open(OUTPUT_FILE, "rb") as f:
            st.download_button("⬇️ Download Logbook Hasil", f, file_name="logbook_selesai.txt")
    except Exception as e:
        st.error(f"❌ Error: {e}")