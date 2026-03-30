# Praktikum 3 Rekayasa Sistem Informasi (RSI) - Desain Database dan ERD

Repositori ini berisi *source code* untuk implementasi basis data relasional pada proyek Sistem Informasi Acara (acara-rsi). Proyek ini dikembangkan sebagai bagian dari tugas Praktikum Rekayasa Sistem Informasi.

## 🛠️ Tech Stack
Proyek ini dibangun menggunakan teknologi berikut:
- **Python 3**
- **Dependency Management:** Poetry
- **Database:** PostgreSQL (berjalan di dalam Docker Container)
- **ORM (Object Relational Mapping):** SQLModel
- **Database Migrations:** Alembic

## 🗄️ Struktur Basis Data
Skema basis data `acara-rsi` terdiri dari 6 entitas utama yang saling berelasi:
- `roles`: Menyimpan tingkat akses pengguna.
- `users`: Menyimpan data profil utama pengguna.
- `accounts`: Menyimpan kredensial autentikasi (username, password) yang berelasi dengan `users` dan `roles`.
- `events`: Menyimpan informasi acara yang tersedia.
- `registrations`: Tabel *junction* untuk mencatat pendaftaran *user* pada suatu *event*.
- `logs`: Mencatat riwayat aktivitas dari setiap akun.

## 🚀 Cara Menjalankan Proyek (Local Setup)

### 1. Prasyarat
Pastikan sistem Anda sudah terinstal perangkat lunak berikut:
- [Docker](https://www.docker.com/) & Docker Compose
- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)

### 2. Menjalankan Database PostgreSQL
Buka terminal di dalam direktori `backend` dan jalankan Docker Compose untuk menyalakan *container* database:
```bash
docker compose up -d
