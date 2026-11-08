---
date: 2026-10-26
title: Mengetahui versi mariadb
categories: [database]
tags: [mariadb]
---
**Mariadb** sebagai salah satu _relational database management system_ yang _open source_ mempunyai dukungan komunitas yang dapat diandalkan. Para pengguna **mariadb** berdiskusi, melaporkan masalah dan memberikan solusi atas masalah pengguna lainnya. Dalam interaksi ini, identifikasi versi **mariadb** sangatlah penting. Versi yang digunakan sangat terkait dengan fitur ataupun _bug_. Sehingga apabila akan meminta bantuan di forum atau pelaporan _bug_ perlu dituliskan versinya.

**Mariadb** sudah menyediakan _built in command_ untuk mengetahui versinya. Pertama, [login ke mariadb]({% post_url 2026-10-16-login-mariadb %}). Kemudian,

```sql
SELECT VERSION();
```
akan tampil tabel informasi versi **mariadb**-nya.

Selesai.