import streamlit as st

# # 1. Konfigurasi Halaman Dasar
st.set_page_config(page_title="CV Digital Mahasiswa", page_icon="🎓", layout="centered")

# # 2. Membuat Sidebar untuk Input Data
st.sidebar.title("⚙️ Pengaturan Profil")
st.sidebar.write("Masukkan data diri Anda di bawah ini:")

# # Komponen Input Teks
nama = st.sidebar.text_input("Nama Lengkap")
nim = st.sidebar.text_input("NIM")
jurusan = st.sidebar.selectbox("Jurusan", ["Informatika", "Sistem Informasi", "Teknik Elektro"])

# # Komponen Input Teks Area (Multi-baris)
deskripsi = st.sidebar.text_area("Deskripsi Singkat (Bio)")

# # Komponen Input Teks Area untuk Organisasi
organisasi = st.sidebar.text_area("Pengalaman Organisasi")

# # Komponen Logika Kondisional untuk Sertifikasi/Magang
st.sidebar.markdown("---")
punya_pengalaman = st.sidebar.checkbox("Punya Pengalaman Magang/Sertifikasi?")

# # Komponen Upload File (Gambar)
foto_profil = st.sidebar.file_uploader("Unggah Foto Profil (Opsional)", type=["jpg", "jpeg", "png"])

# --- AREA UTAMA (MAIN DASHBOARD) ---
st.title("🎓 Curriculum Vitae Digital")
st.markdown("---") # Membuat garis pembatas horizontal

# 3. Membuat Layout 2 Kolom (Kiri untuk Teks, Kanan untuk Foto)
kolom_kiri, kolom_kanan = st.columns([2, 1])

with kolom_kiri:
    # Menampilkan data menggunakan Typography Streamlit
    st.header(nama)
    st.subheader(f"{jurusan} | NIM: {nim}")
    st.write(deskripsi)

with kolom_kanan:
    # Menampilkan foto jika user mengunggahnya
    if foto_profil is not None:
        st.image(foto_profil, width=200, caption="Foto Profil")
    else:
        st.info("Belum ada foto yang diunggah.")

# # Menampilkan Bagian Pengalaman Organisasi
st.markdown("---")
st.markdown("### 👥 Pengalaman Organisasi")
st.write(organisasi)

# # Menampilkan Bagian Sertifikasi/Magang Secara Kondisional
st.markdown("---")
st.markdown("### 💼 Sertifikasi / Magang")
if punya_pengalaman:
    detail_pengalaman = st.sidebar.text_area("Detail Pengalaman Magang/Sertifikasi", "Tulis detail pengalaman di sini.")
    if detail_pengalaman:
        st.success(detail_pengalaman)
    else:
        st.info("Silakan isi detail pengalaman magang/sertifikasi pada sidebar.")
else:
    st.write("Tidak ada riwayat magang atau sertifikasi.")

# --- BAGIAN KEAHLIAN (SKILLS) ---
st.markdown("---")
st.markdown("### 🔧 Keahlian Teknis")

# Sidebar slider untuk mengatur level skill
st.sidebar.markdown("---")
st.sidebar.subheader("Atur Kemahiran Skill")
skill_python = st.sidebar.slider("Python", 0, 100, 80)
skill_web = st.sidebar.slider("Web Development", 0, 100, 60)
skill_db = st.sidebar.slider("Database", 0, 100, 70)

# Menampilkan indikator visual (Progress Bar) di halaman utama
st.write("Python")
st.progress(skill_python)

st.write("Web Development (HTML/CSS)")
st.progress(skill_web)

st.write("Database (SQL)")
st.progress(skill_db)

# --- BAGIAN KONTAK ---
st.markdown("---")
st.markdown("### 📬 Hubungi Saya")
with st.expander("Klik untuk melihat detail kontak"):
    st.write(f"📧 Email: {nama.lower().replace(' ', '')}@mahasiswa.univ.ac.id")
    st.write(f"🔗 LinkedIn: https://linkedin.com{nama.lower().replace(' ', '')}")
    st.write(f"💻 GitHub: https://github.com{nama.lower().replace(' ', '')}")

# # Komponen Tombol Download CV
st.markdown("---")
data_cv = f"Nama: {nama}\nNIM: {nim}\nJurusan: {jurusan}"
st.download_button(label="📥 Download Data CV", data=data_cv, file_name="cv_app.txt")