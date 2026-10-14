---
date: 2026-10-14
title: Membuat user database baru mariadb
categories: [database]
tags: [mariadb]
---
Demi keamanan, sangat disarankan mengelola database menggunakan _user_ bukan _root_. Membuat _user_ baru di **mariadb** sangat mudah. Pertama, _login_ sebagai _root_ di **mariadb**.
```shell
mariadb -u root -p
```
Di dalam _prompt_ **mariadb**, jalankan
```sql
CREATE USER nama_user IDENTIFIED BY 'tulis_passwordnya_di_sini';
```
Ganti `nama_user` dengan nama _user_ yang akan dibuat dan masukkan _password_-nya di bagian `tulis_passwordnya_di_sini`.