---
date: 2015-06-18
title: InstalL sleuthkit slackware
categories: [forensik, manajemen file]
tags: [sleuthkit]
---
[The Sleuth Kit](https://github.com/sleuthkit) atau disingkat TSK adalah tools digital forensik yang bersifat open source, multiplatform dan text-mode (command line interface). TSK bisa digunakan untuk melakukan analisis pada barang bukti, atau lebih tepatnya citra disk (raw image). Misalnya untuk mengetahui berkas apa saja yang ada di dalam hardisk dan adakah berkas yang dihapus dari hardisk itu.

Dependensi:

- autoconf, automake, libtool
- C/C++ compiler (gcc, gcc++)
- [JDK (opsional)]({% post_url 2015-06-07-install-jdk-slackware %})

Install cukup mudah, kita akan install langsung TSK dari source code yang ada di github

```shell
git clone https://github.com/sleuthkit/sleuthkit.git
cd sleuthkit
./bootstrap
./configure
make
make install
```
Instalasi selesai. Nah, di dalam TSK ini terdapat beberapa tools yaitu:

- mmls
- blkls
- blkcalc
- blkstat
- blkcat

Untuk cara penggunaannya menyusul, insya Allah.
