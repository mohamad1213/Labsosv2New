# 🎓 SIM LABSOS (Sistem Informasi Manajemen Laboratorium Sosial)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.+-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

**SIM LABSOS** adalah aplikasi berbasis web yang dirancang khusus untuk mahasiswa Universitas Nahdlatul Ulama Yogyakarta. Aplikasi ini memiliki fungsi utama sebagai **Sistem Informasi Manajemen Praktik Kerja Lapangan (SIM PKL)** serta berfokus dalam menangani seluruh proses administrasi terkait Laboratorium Sosiologi.

*(Versi yang dikembangkan: `v2` / Informatika 2017)*.

---

## 📑 Daftar Isi
- [Fitur Utama & Hak Akses](#-fitur-utama--hak-akses)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Prasyarat Sistem](#-prasyarat-sistem)
- [Panduan Instalasi](#%EF%B8%8F-panduan-instalasi)
- [Menjalankan Aplikasi](#-menjalankan-aplikasi)
- [Akun Pengujian (Demo)](#-akun-pengujian-demo)
- [Deployment](#-deployment)

---

## 👥 Fitur Utama & Hak Akses

Sistem ini dikembangkan dengan arsitektur **multi-role** (multi hak-akses) yang dilengkapi berbagai fungsionalitas pendukung (seperti pembuatan jurnal kegiatan, catatan, logbook, dan forum diskusi). Terdapat beberapa hak akses (Roles) utama yaitu:

1. **👨‍🎓 Mahasiswa (College Student)**: Dapat mendaftar, membuat laporan dan mengelola kegiatan logbook PKL.
2. **👨‍🏫 Dosen (Lecturer)**: Memantau, mengarahkan, memberikan catatan, serta mengevaluasi proses kegiatan yang dilakukan oleh mahasiswa.
3. **💼 Staf (Staff)**: Mengurus sistem administrasi secara umum dari Laboratorium Sosial.
4. **🏢 Mitra**: Pihak eksternal tempat bernaungnya mahasiswa untuk melakukan kegiatan praktik/magang.

---

## 🛠 Teknologi yang Digunakan

Aplikasi ini dibangun menggunakan beberapa framework dan modul pustaka populer:
- **Core / Backend:** Python 3, Django
- **Database:** PostgreSQL (Production) / SQLite3 (Development)
- **Frontend / Forms Visuals:** Django Crispy Forms (`crispy_bootstrap4`), Bootstrap Datepicker Plus
- **Plugins & Libraries:** 
  - `Pillow` (untuk manajemen unggah foto/gambar)
  - `djangorestframework`
  - `psycopg2` (Konektor database PostgreSQL)
  - `coa-django-countable-field`

---

## 📋 Prasyarat Sistem

Sebelum memulai pengembangan *(development)*, pastikan seluruh program pendukung berikut telah terinstall dengan baik pada komputer Anda:
1. **Python** (Disarankan menggunakan versi `3.4` ke atas). Unduh di [python.org](https://www.python.org/downloads/).
2. **PostgreSQL** (opsional, jika ingin menguji enviroment *Production* di lokal). Panduannya dapat dicek [di sini](https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django).
3. **Package Manager Pip** (`pip`) *(sudah terpasang otomatis dari Python 3)*, dan library **Virtual Environment**.

---

## ⚙️ Panduan Instalasi

Ikuti langkah-langkah di bawah ini untuk mengatur dan meng-clone proyek dari tahap awal hingga siap dijalankan ke mesin lokal Anda (*Localhost*).

### 1. Buat Virtual Environment 
Sangat disarankan memakai Virtual Environment (`venv`) agar library pada sistem OS utama Anda tidak mengalami *conflict/error*.
- **Di sistem Windows:**
  ```bash
  python -m venv env
  env\Scripts\activate
  ```
- **Di sistem Linux / macOS:**
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

### 2. Instalasi Kebutuhan Pustaka (Libraries)
Lakukan sinkronisasi atau install keseluruhan pustaka/package (`pip` modules) yang disediakan dalam file `requirements.txt`:
```bash
pip install -r requirements.txt
```
*(Catatan: Jika ada library yang error, lakukan pembaruan pip dengan perintah `python -m pip install --upgrade pip`).*

### 3. Konfigurasi Database
Project diatur koneksinya pada file di folder `SIM_PKL/settings.py`. Pada environment dev lokal Anda bebas menggunakan *SQLite* (bawaan Django). 
*Note: Jika ingin menggunakan PostgreSQL, ubah parameter koneksi DB pada blok variabel `DATABASES`.*

### 4. Lakukan Migrasi Database (*Migration*)
Wajib untuk dijalankan sebelum pertama kali aplikasi dibuka agar arsitektur DB lengkap:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🚀 Menjalankan Aplikasi

Setelah semua instalasi dan DB ter-migrasi sukses, Anda dapat merestart server percobaan Django (*development server*):

```bash
python manage.py runserver
```

Akses secara lokal aplikasi melalui peramban (Web Browser) di alamat server:
👉 **`http://localhost:8000/`** atau **`http://127.0.0.1:8000/`**

---

## 🔑 Akun Pengujian (Demo)

*(Opsional: apabila Anda memakai dump SQL database bawaan)*. Anda dapat login ke dalam web SIM LABSOS memakai rincian percobaan berikut:

**👨‍🎓 College Student (Mahasiswa)**
- Username / Akun: `user`
- Password / Sandi: `praxis123`
*(Bisa juga menggunakan fitur Register / Sign Up baru pada aplikasi)*

**👨‍🏫 Lecturer (Dosen)**
- Username / Akun: `prof.tatam`
- Password / Sandi: `praxis123`

**💼 Staff / Administrasi**
- Username / Akun: `staf`
- Password / Sandi: `praxis123`

---

## 📸 Screenshot Aplikasi

Berikut adalah beberapa tampilan dari aplikasi SIM LABSOS:

![Halaman Login](media/screenshots/login.png)
*Gambar 1: Halaman Login*

![Dashboard Mahasiswa](media/screenshots/dashboard_mahasiswa.png)
*Gambar 2: Dashboard Mahasiswa*

![Halaman Forum Diskusi](media/screenshots/forum_diskusi.png)
*Gambar 3: Halaman Forum Diskusi*

---

## 📝 Keterangan Fitur

Berikut adalah fitur-fitur utama yang tersedia di aplikasi SIM LABSOS:

1. **Manajemen Akun**
   - Registrasi dan autentikasi pengguna.
   - Reset password melalui email.

2. **Logbook PKL**
   - Mahasiswa dapat mencatat kegiatan harian selama PKL.
   - Dosen dapat memberikan evaluasi dan catatan pada logbook.

3. **Forum Diskusi**
   - Fasilitas diskusi antara mahasiswa, dosen, dan staf.
   - Mendukung unggahan file dan komentar.

4. **Manajemen Catatan**
   - Dosen dan staf dapat membuat catatan penting terkait kegiatan mahasiswa.

5. **Dashboard Interaktif**
   - Statistik dan ringkasan kegiatan mahasiswa.
   - Notifikasi untuk tugas atau catatan baru.

6. **Manajemen Mitra**
   - Informasi dan pengelolaan mitra tempat mahasiswa melakukan PKL.

---

## 🌍 Deployment

Sistem telah siap dan sangat mendukung integrasi *deployment* ke Cloud Platform seperti **Heroku**. Konfigurasi platform (*Procfile*) telah diletakkan di dalam direktori dasar proyek.
- URL Pengujian Deployment Aplikasi: [https://labsosv2.herokuapp.com/](https://labsosv2.herokuapp.com/)
