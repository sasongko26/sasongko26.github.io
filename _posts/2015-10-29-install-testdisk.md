---
date: 2015-10-29
title: Install testdisk
categories: [forensik]
tags: [testdisk]
---
Testdisk adalah salah satu aplikasi *digital* forensik multiplatform. Bisa dijalankan di Windows (NT4, 2000, 2003, XP, Vista dan 7), Linux, FreeBSD, OpenBSD, NetBSD, SunOS, dan MacOS. Adapun kegunaannya untuk mengembalikan partisi yang terhapus beserta file-file yang ada di dalamnya. Informasi lebih lengkap tentang testdisk bisa didapatkan di [sini](https://www.cgsecurity.org/).

Sebenarnya untuk Slackware sudah ada *slackbuild*-nya, tapi tidak ada salahnya kalau install dari kode sumber. Penginstallan dijalankan dengan level root.

```shell
wget http://www.cgsecurity.org/testdisk-7.0.tar.bz2
tar xjvf testdisk-7.0.tar.bz2
cd testdisk-7.0 
./configure
make
make install
```

Oke, testdisk sudah diinstall. Untuk mulai menjalankannya (harus level root)

```shell
testdisk
```
