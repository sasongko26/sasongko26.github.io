---
date: 2022-03-01
title: Konfigurasi mirror slackware
categories: [manajemen paket]
tags: [slackpkg]
---
**Slackpkg** merupakan salah satu **official slackware package manager**. Fitur yang dimilikinya antara lain

1.  Cek apakah ada update
2.  Baca changelog
3.  Install, upgrade, reinstall, remove, blacklist packages

Sebelum menggunakannya, pilih dahulu *mirror* yang akan digunakan
```shell
vi /etc/slackpkg/mirrors
```
Pada file tersebut sudah tersedia list mirror yang bisa digunakan. Apakah menggunakan **current** atau **stable** (saat ini 15.0). Pilih mirrornya dengan cara *uncomment* baris alamat mirrornya. Contoh

```shell
https://mirrors.slackware.com/slackware/slackware64-15.0/
```

untuk menggunakan mirror terdekat versi **slackware 15.0**.
