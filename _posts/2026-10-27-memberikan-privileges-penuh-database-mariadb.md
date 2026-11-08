---
date: 2026-10-27
title: Memberikan privileges penuh atas database
categories: [database]
tags: [mariadb]
---
Secara _default_, **mariadb** hanya memberikan akses atau _privileges_ secara penuh atas database hanya kepada **root**. Jika _user_ lain ingin mendapatkannya maka ia harus diberikan _all privileges_. Adanya _all privileges_ membuat _user_ semakin berkuasa. Perlu kecermatan dalam pemberian ini karena hak aksesnya semakin bertambah. Pastikan hanya orang terpercaya yang diberikan kewenangan untuk menggunakan akun terseut.

Untuk memberikan hak akses penuh atau _all privileges_ atas suatu database, pertama [login dulu ke mariadb]({% post_url 2026-10-18-login-mariadb %}. Kemudian

```sql
GRANT ALL PRIVILEGES ON nama_database.* TO 'nama_pengguna'@'localhost';
```

silakan ganti `nama_database` dengan nama database yang akan diberikan hak atasnya, dan `nama_pengguna` dengan nama _user_ yang akan diberikan hak aksesnya.

Selesai.