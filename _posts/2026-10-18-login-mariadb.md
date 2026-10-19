---
date: 2026-10-18
title: Login mariadb
categories: [database]
tags: [mariadb, login]
---
Manajemen database dengan **mariadb** membutuhkan akses akun atau _user_ **mariadb**. Akses penuh dimiliki oleh **root**. Namun, untuk keamanan disarankan menggunakan _user_ selain **root**.

**Mariadb** membuat skenario bisa login menggunakan akun _user_ yang ada di sistem operasi (misal **Slackware Linux** yang kami gunakan sehari-hari) dengan _password_ yang sama. Jika login ke user yang sama bisa langsung jalankan

```shell
mariadb
```

Tetapi, kalau ingin login dengan _user_ yang berbeda, tambahkan opsi `-u` diikui nama _user_ dan opsi `-p` kemudian masukkan _password_-nya.

```shell
mariadb -u nama_user -p
```

Ganti `nama_user` dengan nama _user_ yang ingin dituju sebagai loginnya.

Selesai.