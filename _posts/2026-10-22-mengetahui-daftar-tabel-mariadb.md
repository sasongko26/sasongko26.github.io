---
date: 2026-10-22
title: Mengetahui daftar tabel mariadb
categories: [database]
tags: [mariadb]
---
Database tersusun atas tabel. Tanpa tabel database tersebut adalah database kosong. Untuk mengecek apakah database tersebut kosong atau tidak beginilah caranya.

Pertama, login **mariadb**
```shell
mariadb
```
 atau
 ```shell
 mariadb -u root -p
 ```
 untuk login sebagai root mariadb karena biasanya semua database dikuasai oleh akun root.

Setelah masuk ke dalam _prompt_ **mariadb**
```sql
USE nama_database;
```
ganti `nama_database` dengan database yang akan dicek tabelnya. Kemudian jalankan
```sql
SHOW TABLES;
```
akan terlihat tabel yang ada di dalam database tersebut.

Selesai.