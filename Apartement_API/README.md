# 🏢 Aplikasi Booking Apartemen - Fullstack Hybrid (API + HTML)

Selamat datang di aplikasi **Booking Apartemen** — platform pemesanan apartemen harian dan jam-jaman yang cepat, modern, dan fleksibel!  
Aplikasi ini menggabungkan **Flask API (Backend)** dengan **HTML Bootstrap UI (Frontend)**, sehingga cocok untuk demo **fullstack hybrid**.

---

## 📁 Struktur Folder
APARTEMENT_API
├── app.py # Entry point utama Flask
├── extension.py # Setup database & JWT
├── models.py # Model database (User, Apartment, Booking)
├── requirements.txt      
├── Procfile
│
├── routes/ # Semua blueprint Flask
│ ├── auth.py # Register, login, logout
│ ├── bookings.py # Booking apartemen (API + tampilan)
│ └── apartements.py # Data apartemen (API)
│
├── templates/ # Tampilan HTML (Jinja2)
│ ├── index.html # Beranda / Homepage
│ ├── login.html # Form login
│ ├── register.html # Form daftar akun
│ ├── booking_list.html # Daftar apartemen tersedia
│ └── booking_detail.html # Detail & harga per apartemen
│
└── static/
    ├── images/ # Gambar apartemen
    └── css/ # Styling tambahan

---

## 🎯 Fitur Unggulan

### ✅ **Frontend (User Interface):**
- Hero banner dengan tombol `Lihat Apartemen`, `Daftar`, dan `Masuk`
- Tampilan apartemen dengan **gambar + nama + tombol Lihat Detail**
- Deskripsi lengkap setiap apartemen: lokasi, harga jam-jaman, malam, full-day
- Tombol **Hubungi Sekarang (WhatsApp)** langsung ke nomor admin
- **Navbar dinamis**: menampilkan nama user setelah login

### ✅ **Backend (Flask API):**
- `POST /api/register` → Daftar user baru
- `POST /api/login` → Login dan simpan ke `session`
- `GET /api/apartments` → Ambil daftar apartemen (JSON)
- `GET /api/bookings` → Ambil list booking user
- `POST /api/bookings` → Buat booking (hanya via token JWT)

---

## 👥 Teknologi yang Digunakan

| Komponen         | Teknologi                                  |
|------------------|--------------------------------------------|
| Backend API      | Flask, SQLAlchemy, JWT                     |
| Frontend         | HTML + Bootstrap 5 + Jinja2                |
| Database         | SQLite3 (bisa diubah ke PostgreSQL/MySQL)  |
| Autentikasi      | JWT + Flask-Session (hybrid)               |
| Deployment-ready | Bisa dipublish ke Render / Railway         |

---

## 🚀 Cara Menjalankan Project

### 1. **Clone / Download Project**
```bash
git clone https://github.com/mhmmdikmal09/Apartement_API.git
cd Apartement_API

LANGKAH LANGKAH
1.
python -m venv venv
venv\Scripts\activate  # Windows

2.
pip install -r requirements.txt

3.
python app.py


🔑 Langkah Pemakaian
- Register akun melalui tombol Daftar
- Login menggunakan email dan password
- Tampilan berubah otomatis → muncul “Halo, [Nama]” dan tombol Logout
- Klik tombol Mulai Booking Sekarang
- Pilih salah satu apartemen → klik Lihat Detail
- Akan muncul info lengkap dan tombol Hubungi Sekarang (WhatsApp)


📝 Kesimpulan Project
Aplikasi ini dirancang dengan arsitektur hybrid — menggabungkan kekuatan REST API dan tampilan HTML.
Tujuannya adalah memberikan fleksibilitas bagi user, sambil menjaga kemudahan deploy dan presentasi.

🔸 Cocok untuk demo portofolio developer fullstack
🔸 Desain clean dan profesional (dengan Bootstrap)
🔸 Bisa dengan mudah dikembangkan menjadi full marketplace

👋 Dibuat oleh
Ikmal — Fullstack Developer & Business Visionary
💼 Tujuan: Digitalisasi sistem sewa apartemen harian dan bulanan