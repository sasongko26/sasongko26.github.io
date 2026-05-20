---
date: 2017-01-14
title: Enkripsi file dengan gnupg
categories: [keamanan, forensik]
tags: [gpg]
---
Selain dengan [openssl]({% post_url 2017-01-08-enkripsi-dg-openssl %}), enkripsi file juga dapat dilakukan dengan gnupg atau yang biasa disebut dengan gpg.

```shell
gpg -o file_hasil_enkripsi -c file_yang_akan_dienkripsi
```
Sedangkan untuk dekripsi

```shell
gpg -o file_hasil_dekripsi -d file_yang_akan_didekripsi
```

