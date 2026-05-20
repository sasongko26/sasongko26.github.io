---
date: 2019-04-20
title: Reverse dependency sbopkg
categories: [manajemen paket]
tags: [sbopkg]
---
ecara *default* sbopkg tidak menyediakan fitur **reverse dependency**. Adapun untuk butuh *dependency*-nya apa saja bisa menggunakan sqg. Bagaimana tahu *reverse dependency*-nya? Ini cara sederhana yang saya gunakan

```shell
grep -w REQUIRES /var/lib/sbopkg/SBo/*/*/*/*.info | grep -w nama_paket
```

Dengan cara tersebut bisa diketahui suatu paket/*package* itu menjadi dependensi dari paket apa. Tapi, salah 1 dari *output* tersebut tidak lain adalah paket itu sendiri. Dan, *package* yang ditampilkan adalah semua yang ada di SBo. Kita masih perlu memeriksa apakah *packages* tersebut terinstall atau tidak.
