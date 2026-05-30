---
date: 2021-01-01
title: Menggunakan rsync
categories: [jaringan]
tags: [rsync]
---
# Kegunaan rsync
**rsync** berguna untuk transfer file secara efisien. Dibandingkan dengan **cp** atau **mv**, **rsync** memiliki keunggulan :

1.  Bebas pilih-pilih file maupun direktori yang akan ditransfer karena ada fitur *include* dan *exclude*
2.  Apabila gagal, misalnya karena *storage* penuh atau “kecelakaan” salah klik sehingga ter-*close*, dapat dilanjutkan tanpa mengulang dari awal sehingga waktunya tentu lebih cepat

Dibandingkan **wget**, **rsync** mendukung penggunaan *wildcard* dan secara *default* **rsync** *resumeable*.

Akan dilakukan transfer/copas semua yang ada di /media/hd0 ke /media/hd1

```shell
rsync -arvz --progress /media/hd0/ /media/hd1/
```
Opsi **-arvz** diberikan untuk archive, recursive, verbose dan kompres(z). Sementara **–progress** untuk menampilkan progress sejauh mana file tersebut ditransfer. Bila asal hanya /media/hd0 (tanpa diakhiri /), maka artinya sama saja dengan tujuannya adalah /media/hd1/hd0/


