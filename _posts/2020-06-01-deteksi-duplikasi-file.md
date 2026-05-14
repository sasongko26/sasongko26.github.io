---
date: 2020-06-01
title: Deteksi duplikasi file
categories: [manajemen file]
tags: [sha512sum, awk, uniq]
---
Walau sudah ada *tools* yang secara langsung mengetahui duplikasi file di linux, saya lebih suka menggunakan *tools* bawaan **Slackware**. *Tools* yang umum digunakan antara lain fslint, fdupes atau jdupes. Adapun *tools* yang biasa saya gunakan

1.  sha512sum
2.  awk
3.  uniq
4.  grep

Misalkan, akan mencari adakah duplikasi file di folder Downloads. Pertama, catat dulu *hash*-nya. Di sini saya gunakan *sha512*. Kumpulan *sha512* tersebut disatukan dalam file downloads.sha512. File ini terdiri dari 2 kolom. Kolom pertama berisi *hash*, sedangkan kolom kedua nama filenya.

```shell
sha512sum Downloads/* > downloads.sha512
```

Selanjutnya difilter berdasarkan *hash* atau kolom pertama yang kemudian dicek keunikannya. Kalau ada *hash* yang sama akan tampil karena menunjukkan file yang sama.

```shell
awk '{ print $1 }' downloads.sha512|uniq -d
```

Kemudian, untuk mengetahui file mana saja yang sama, sesuaikan hashnya

```shell
grep "[tulis hash nya di sini]" downloads.sha512 
```
