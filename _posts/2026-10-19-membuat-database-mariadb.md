---
date: 2026-10-19
title: Membuat database mariadb
categories: [database]
tags: [mariadb]
---
Membuat database baru dengan **mariadb** sangat mudah. Pertama, [login dulu]({% post_url 2026-10-18-login-mariadb %}). Kemudian setelah masuk ke _prompt_ **mariadb**

```sql
CREATE DATABASE nama_database;
```

Ganti `nama_database` dengan nama database yang akan dibuat. Contoh, untuk membuat database bernama perpustakaan

```sql
CRETAE DATABASE perpustakaan;
```

Selesai.