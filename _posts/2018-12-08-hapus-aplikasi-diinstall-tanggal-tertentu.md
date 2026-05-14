---
date: 2018-12-08
title: Hapus Aplikasi yang Diinstall Tanggal Tertentu
categories: [manajemen file]
tags: [removepkg, find]
---
Tiga hari ini mencoba-coba install kdenlive, aplikasi editor video yang konon handal. Sengaja disebut konon karena belum membuktikannya secara langsung. Setelah semua beres diinstall ternyata malah berubah pikiran. Apa perlu saya pakai editor video? Toh selama ini tidak pernah edit video dan pekerjaan sehari-hari juga tidak bersentuhan langsung dengan pembuatan maupun *editing* video. Jadi hapus sajalah.

kdenlive-nya sukses di-*uninstall*, tapi bagaimana dengan seabrek dependensinya? Hapus juga deh! Kalau besok-besok diperlukan tinggal install lagi.

Terlintas di pikiran kalau identifikasi dependensinya satu-persatu, dari file .info SBo, tapi sepertinya repot karena banyak. Untungnya saya punya kebiasaan untuk install aplikasi itu harian. Maksudnya gini. Install 1 aplikasi (utama) 1 hari. Kalau ada dependensinya diinstall di hari itu juga. Alhamdulillah juga masih ingat kapan diinstallnya yaitu 3 hari yang lalu. Jadi bisa pakai find.

```shell
find /var/lib/pkgtools/packages/ -type f -mtime 3 -exec removepkg {} +
```
