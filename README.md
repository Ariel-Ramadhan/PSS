# UTS Pemrograman Sisi Server — Flask + MySQL + Docker Compose
# Ariel Ramadhan Diva Aretha Putra Retnawan | A11.2022.14297

## Deskripsi
Aplikasi CRUD User dan Produk menggunakan Flask dan MySQL.
Dijalankan dengan arsitektur multi-container (web + database) menggunakan Docker Compose.

## Struktur
- `web`: Aplikasi Flask (Python)
- `db`: MySQL Server
- `db_data`: Volume untuk menyimpan data agar tidak hilang

## Cara Menjalankan
1. Pastikan Docker dan Docker Compose sudah terinstal.
2. Jalankan:
   ```bash
   docker compose up -d --build
3. Lalu jalankan http://localhost:5000/ di browser.
