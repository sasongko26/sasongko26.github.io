---
date: 2026-10-13
title: Menampilkan user database mariadb
categories: [database]
tags: [mariadb]
---
Manajemen database sangat disarankan menggunakan akun/_user_ bukan _root_ demi keamanan. Untuk mengetahui _user_  yang ada di **mariadb** jalankan
```shell
mariadb -u root -p
``
masukkan _password_, kemudian setelah masuk **mariadb**,
```sql
SELECT User FROM mysql.user;
```
akan tampil semua _user_ database **mariadb**.