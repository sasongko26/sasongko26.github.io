---
date: 2021-11-30
title: Mengetahui banyaknya elemen array perl
categories: [pemrograman]
tags: [perl]
---
*Array* adalah salah satu tipe data pada **bahasa pemrograman perl**. Tipe data ini berisi data majemuk. Penulisan *array* menggunakan notasi @.

Contoh:
```perl
my @buah = ("pepaya", "manga", "pisang", "jambu", "durian", "apel");
```

Untuk mengetahui berapa banyaknya elemen dari *array*, bisa menggunakan **scalar()**.

```perl
print(scalar(@buah));
```
