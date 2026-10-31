---
date: 2026-10-24
title: Mengenal privileges user mariadb
categories: [database]
tags: [mariadb]
---
**Mariadb** mengenal adanya hak akses atau _privileges_ yang melekat pada _user_. Hak tersebut terkait dengan manajemen database. _Privileges_ tersebut antara lain:

1. SELECT untuk membaca data
2. INSERT untuk menambah data baru
3. UPDATE untuk mengubah data
4. DELETE untuk menghapus data
5. CREATE untuk membuat database/data
6. DROP untuk menghapus database/tabel
7. ALTER untuk mengubah struktur tabel
8. INDEX untuk membuat atau menghapus index
9. REFERENCES untuk membuat _foreign key_

Dengan adanya _privileges_ tersebut memungkinkan manajemen data secara selektif dan proporsional. Selektif maksudnya suatu _user_ mempunyai hak akses sendiri yang bisa berbeda dengan _user_ lainya. Proporsional, manajemen database yang dilakukan _user_ adalah sesuai dengan _privileges_ yang diberikan kepadanya.