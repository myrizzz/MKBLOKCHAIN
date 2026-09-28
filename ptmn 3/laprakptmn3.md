# Halal Coffee Supply Chain Blockchain Explorer

Aplikasi berbasis blockchain simulasi untuk mencatat dan memverifikasi integritas data rantai pasok kopi halal. Proyek ini dibangun menggunakan Python dengan antarmuka Streamlit untuk memastikan transparansi data agar tidak dapat dimanipulasi (tamper-proof).

---

## Struktur File

Proyek ini terdiri dari dua modul utama:
1. *core.py*: Berisi arsitektur dasar blockchain, logika enkripsi SHA-256, dan fungsi validasi integritas data.
2. *app.py*: Berisi antarmuka pengguna berbasis web untuk menginput data rantai pasok dan menampilkan buku besar (ledger).

---

## Mekanisme Kerja core.py

Modul core.py berfungsi sebagai mesin utama penyusun blockchain yang terdiri dari dua komponen:

### 1. Class Block
Merepresentasikan satu unit data atau satu rekaman transaksi dalam rantai pasok. Komponennya meliputi:
* *index*: Nomor urut blok di dalam rantai.
* *timestamp*: Catatan waktu otomatis saat blok dibuat dalam format Unix.
* *timestamp_readable*: Properti untuk mengubah format waktu Unix menjadi format waktu lokal (YYYY-MM-DD HH:MM:SS) agar mudah dibaca.
* *data*: Informasi utama rantai pasok yang disimpan (Aktor, Jumlah Panen, Lokasi).
* *prev_hash*: Hash dari blok sebelumnya yang berfungsi sebagai pengikat antarblok.
* *hash*: Kode enkripsi SHA-256 unik hasil kalkulasi dari gabungan seluruh data di dalam blok tersebut.

### 2. Class Blockchain
Berfungsi sebagai pengelola seluruh kumpulan blok. Fitur utamanya meliputi:
* *create_genesis_block*: Membuat blok pertama secara otomatis (Genesis Block) saat sistem diinisialisasi.
* *add_block*: Menambahkan data baru ke dalam rantai dengan mengambil hash dari blok terakhir sebagai komponen pembentuk hash blok baru.
* *is_chain_valid*: Melakukan audit total terhadap seluruh rantai dari awal hingga akhir untuk memastikan tidak ada data yang diubah.

---

## Fitur Keamanan dan Validasi

Fungsi is_chain_valid memeriksa dua hal utama untuk mendeteksi manipulasi data:

| Jenis Pemeriksaan | Cara Kerja | Fungsi |
| :--- | :--- | :--- |
| *Konsistensi Hash* | Sistem menghitung ulang hash blok berdasarkan datanya saat ini dan mencocokkannya dengan nilai hash yang tersimpan. | Mendeteksi jika ada perubahan karakter atau angka pada isi data secara sepihak. |
| *Keterkaitan Rantai* | Sistem memeriksa apakah nilai prev_hash blok saat ini sama dengan nilai hash milik blok sebelumnya. | Mendeteksi jika ada upaya penyisipan, penghapusan, atau penukaran urutan blok. |

Jika salah satu pemeriksaan tersebut gagal, sistem akan mendeteksi status rantai tidak valid dan memicu peringatan manipulasi data pada antarmuka web.

---

## Cara Menjalankan Aplikasi

1. Pastikan library Streamlit sudah terinstal:
   bash
   pip install streamlit
   
2. Pastikan file core.py dan app.py berada dalam satu direktori yang sama.
3. Jalankan perintah berikut melalui terminal:
   bash
   streamlit run app.py