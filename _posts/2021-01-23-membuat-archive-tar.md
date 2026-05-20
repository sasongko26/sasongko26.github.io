---
date: 2021-01-23
title: Membuat archive tar
categories: [manajemen file]
tags: [tar]
---
Terdapat file sebagai berikut:

```shell
Screenshot_2020-07-15_10-17-33.png
Screenshot_2020-08-03_10-31-47.png
Screenshot_2020-08-04_16-33-18.png
Screenshot_2020-08-06_08-22-59.png
Screenshot_2020-08-06_08-31-22.png
Screenshot_2020-12-04_18-44-18.png
Screenshot_2021-01-12_01-21-31.png
```

Ketujuh file tersebut akan disatukan dalam 1 *archive* dengan nama file *screenshot.tar.gz*.

```shell
tar cvf screenshot.tar.gz Screen*
Screenshot_2020-07-15_10-17-33.png
Screenshot_2020-08-03_10-31-47.png
Screenshot_2020-08-04_16-33-18.png
Screenshot_2020-08-06_08-22-59.png
Screenshot_2020-08-06_08-31-22.png
Screenshot_2020-12-04_18-44-18.png
Screenshot_2021-01-12_01-21-31.png
```

Penjelasan *command*

- tar : manajemen *archive* yang digunakan aalah *tar*
- c : wajib dituliskan untuk *create* atau membuat *archive*
- v : opsi untuk *verbose*, menampilkan list file yang diproses
- f : wajib dituliskan dalam semua penggunaan *tar* karena f adalah file, identifier untuk file yang akan diproses
- screenshot.tar.gz : nama file *archive*. Ekstensi bisa .tar, .tar.gz, atau .tar.xz. Ketika ekstensi ini sering dipakai di dunia *open source*.
- Screen\* : file yang akan di-*archive*. Karena filenya banyak dan mempunyai kemiripan pola maka digunakan *regex* agar lebih praktis. File ini juga bisa dituliskan satu persatu.

