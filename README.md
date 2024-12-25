# Klasifikasi-Performa-Siswa
Nama : Galvan Adam Maliki (202110370311188)

Repository ini dibuat untuk memenuhi Tugas Akhir Praktikum Mata Kuliah Pembelajaran Mesin

Model dapat di akses di Drive Berikut:
https://drive.google.com/drive/folders/1EiguGjtqK0kDXC8D5cI0mUNxCOLy_djB?usp=sharing

# Klasifikasi Performa Siswa Berdasarkan Nilai Mata Pelajaran

## Deskripsi Project
Aplikasi ini bertujuan untuk mengklasifikasikan performa siswa berdasarkan nilai mata pelajaran yang diinputkan oleh pengguna. Dengan menggunakan algoritma pembelajaran mesin, aplikasi ini dapat memberikan label performa seperti "Baik", "Cukup", atau "Kurang" berdasarkan rata-rata nilai siswa.

## Latar Belakang
Pendidikan adalah fondasi penting dalam pengembangan individu. Menilai performa siswa secara objektif dapat membantu para pendidik dalam memberikan perhatian yang sesuai terhadap kebutuhan masing-masing siswa. Proyek ini dibuat untuk membantu analisis performa siswa secara otomatis dan memberikan wawasan yang bermanfaat bagi pendidik dan siswa.

## Fitur Proyek
1. **Input Data Nilai Siswa**: Pengguna dapat menginputkan data nilai untuk beberapa mata pelajaran.
2. **Klasifikasi Performa**: Sistem akan mengklasifikasikan performa siswa berdasarkan rata-rata nilai yang dihitung.
3. **Visualisasi Hasil**: Data hasil klasifikasi ditampilkan dalam bentuk tabel dan grafik untuk analisis yang lebih mudah.
4. **Penyimpanan Sementara**: Data yang dimasukkan pengguna disimpan selama sesi aplikasi berlangsung.

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama untuk membangun aplikasi.
- **Streamlit**: Framework untuk membangun antarmuka pengguna berbasis web.
- **Scikit-learn**: Library untuk pembelajaran mesin.
- **Pandas**: Untuk manipulasi dan analisis data.
- **Matplotlib dan Seaborn**: Untuk visualisasi data.
- **Joblib**: Untuk memuat model pembelajaran mesin yang telah dilatih.

## Alur Proyek
1. **Input Data**: Pengguna menginputkan nilai mata pelajaran seperti IPA, IPS, Matematika, Sejarah, Fisika, dan Kimia.
2. **Hitung Rata-rata**: Sistem menghitung rata-rata nilai siswa.
3. **Klasifikasi Performa**: Sistem mengklasifikasikan performa siswa menggunakan fungsi yang telah ditentukan.
4. **Tampilkan Hasil**: Hasil klasifikasi ditampilkan dalam tabel dan visualisasi.

## Cara Menggunakan
1. Pastikan Anda memiliki Python dan semua library yang diperlukan sudah diinstal.
2. Jalankan aplikasi menggunakan perintah berikut di terminal:
   ```bash
   streamlit run app.py
   ```
3. Pada halaman utama, pilih opsi **Input Data** untuk memasukkan data siswa.
4. Setelah data diinputkan, navigasikan ke halaman **Hasil Klasifikasi** untuk melihat hasil klasifikasi dan visualisasinya.

