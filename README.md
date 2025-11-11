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
   docker compose up -d 

3. Lalu untuk memastikan flask_mysql_db dalam keadaan UP:
   ```bash
   docker ps

4. Tunggu beberapa saat sekitar 20 detik

5. Lalu lakukan login ke mysql dengan password (rootpass123):
   ```bash
   docker exec -it flask_mysql_db mysql -u root -p

6. Lalu jalankan http://localhost:5000/ di browser.
