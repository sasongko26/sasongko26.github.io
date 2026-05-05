---
date: 2026-04-24
title: Menggunakan slackpkg install-new
categories: [manajemen paket]
tags: [slackpkg]
---
Proyek _open source_ dikembangkan secara dinamis. Suatu saat ditambah fitur. Saat yang lain diperbaiki _error_-nya. Saat yang lain lagi ditambal celah keamanannya. Begitu juga dengan **slackware**. Suatu saat ada perubahan. Perubahan tersebut berupa paket yang _upgraded, added, rebuilt, removed_.  Perubahan tersebut disimpan di suatu catatan yang disebut changelog. Changelog **slackware** bisa ditemukan di /var/lib/slackpkg/ChangeLog.txt atau dengan menjalankan `slackpkg show-changelog`.

Saat _ChangeLog.txt_ ada paket yang ditambahkan (_added_), seperti contoh berikut, (bagian bertitik-titik adalah bagian dari changelog yang tidak ditampilkan)

```text
......
l/python-vcs_versioning-1.1.1-x86_64-1.txz:  Added.
......
x/libdecor-0.2.5-x86_64-1.txz:  Added.
```

Kita bisa menginstall mereka sekaligus, atau satu-persatu. Jika ingin menginstallnya secara massal, jalankan

```bash
slackpkg install-new
```

kemudian akan muncul daftar paket baru yang siap diinstall. Pilih `Ok` atau tempatkan _pointer_ di `Ok` tekan `Enter`.

Jika hanya sebagian yang akan diinstall, jangan langsung `Ok`, tetapi pilih dahulu paket mana yang akan diinstall. Cara memilihnya dengan memberikan tanda di paket itu. Tekan `spacebar` atau `spasi` untuk mengaktifkan/memilih dan mengosongkan pilihan. Atau, bisa juga dengan `slackpkg install` diikuti nama paketnya, contoh

```bash
slackpkg install libdecor
```
