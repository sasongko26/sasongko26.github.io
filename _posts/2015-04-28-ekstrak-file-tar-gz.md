---
date: 2015-04-28
title: Ekstrak file .tar.gz
categories: [manajemen file]
tags: [tar]
---
Kemarin di grup facebook Ubuntu Indonesia ada yang bertanya yang intinya

> Bagaimana cara install file .tar.gz?

File dengan ekstensi tar.gz adalah file kompresi/arsip. ‘Saudara’ dari tar.gz yang juga sering dijumpai adalah [zip]({% post_url 2015-05-13-ekstrak-file-zip %}). Atau, bagi yang sebelum memakai linux sudah sangat familiar dengan Windows, tar.gz ini mirip dengan rar.

Nah, file kompresi ini *bukanlah* file installer, tetapi **bisa jadi** mengandung file installer. File installer di linux ada berbagai macam ekstensinya, contoh deb, rpm, tgz, dan sh. Tiap file installer itu mempunyai cara install yang beda. Untuk menginstallnya tentu saja tergantung dari isi file tar.gz itu tadi.

Bagaimana ekstrak file tar.gz?

```shell
tar xzf namafile.tar.gz
```
