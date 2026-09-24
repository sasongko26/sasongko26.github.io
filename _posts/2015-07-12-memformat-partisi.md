---
date: 2015-07-12
title: Memformat Partisi
categories: [manajemen file]
tags: [mkfs]
---

Melanjutkan catatan \kemarin]({% post_url 2015-07-11-membuat-partisi-dengan-cgdisk %}) sekarang partisinya diformat menjadi ext4, format filesystem yang umum digunakan untuk linux dengan kestabilan yang tidak diragukan lagi.

Partisi yang akan diformat ext4 adalah /dev/sda9 dan akan diberi label sebagai src. Pemformatan ini juga harus dilakukan root.

```shell
 mkfs -t ext4 -L 'src' /dev/sda9
```
