---
date: 2026-04-23
title: Membaca changelog slackware
categories: [manajemen paket]
tags: [slackpkg,changelog]
---
# Apa itu changelog

_Open source software_ (OSS) memiliki karakteristik kode sumbernya dapat dibaca oleh umum. Biasanya tidak hanya kode sumbernya yang dibuka, tetapi juga riwayat proyek tersebut. Kapan dirilis dan tanggal sekian ada perubahan apa. Apakah ada penambahan fitur, peningkatan versi, perbaikan _bug_ atau penambalan masalah _security_. Perubahan-perubahan tersebut dicatat ke dalam file yang disebut _changelog_. Tidak aturan resmi atau ijma' alias kesepakatan terkait penamaan dan lokasi file ini. Sehingga, setiap proyek OSS bebas memberikan nama dan penempatannya. Patrick J. Volkerding _developer_ sekaligus _maintainer_ **slackware** memberikan nama file **ChangeLog.txt**. File ini ada di direktori `/var/lib/slackpkg`.

# Cara membaca changelog

**ChangeLog.txt** adalah file teks, sehingga untuk membacanya bisa menggunakan teks viewer seperti `cat, less`, dan `more`. Teks editor seperti `vim, emacs, nano` pun dapat digunakan untuk membacanya. Kami menyarankan untuk menggunakan `less` karena file **ChangeLog.txt** semamin lama semakin panjang.

```bash
less /var/lib/slackpkg/ChangeLog.txt
```

Perlu diperhatikan bahwa **ChangeLog.txt** ini hanya mencatat perubahan paket standar, yaitu paket yang secara _official_ ada di repo **slackware**. File ini menjadi bagian yang tak terpisahkan dengan `slackpkg`. Sehingga membacanya juga bisa menggunakan `slackpkg`.

```bash
slackpkg show-changelog
```
