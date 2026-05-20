---
date; 2017-01-08
title: Enkripsi File dengan OpenSSL
categories: [keamanan, forensik]
tags: [openssl]
---
Salah satu yang membuat saya kepincut menggunakan GNU/Linux yaitu mudahnya mengamankan file. Salah satu caranya adalah dengan enkripsi. Di sini saya gunakan openssl. Cara lainnya yang dapat digunakan adalah dengan [gpg]({% post_url 2017-01-14-enkripsi-dg-gpg %}).

Contoh, saya punya file yang perlu diamankan. Katakanlah filenya indonesia-raya.odt. Saya enkripsi menggunakan openssl dengan *cipher rc4*. File hasil enkripsi saya namai rahasia.odt yang saya taruh di fd dan fd saya mount di /media/hd0. Kemudian akan ditanya *password* enkripsinya.

```shell
openssl enc -e -rc4 -in indonesia-raya.odt -out /media/hd0/rahasia.odt
enter rc4 encryption password:
Verifying - enter rc4 encryption password:
```
Untuk mendekrip, tambahkan opsi -d kemudian masukkan *password*-nya.

```shell
openssl enc -d -rc4 -in /media/hd0/rahasia.odt -out indonesia-raya.odt
```
