---
date: 2026-04-20
title: Mengenal slackbuilds
categories: [manajemen paket]
tags: [slackbuild]
---
_Slackbuilds_ berperan penting dalam instalasi atau pemasangan paket atau _software_ di **slackware** karena merupakan skrip barisan perintah untuk membuat paket biner. _Slackware builds script_ nama lengkapnya. Patrick Volkerding membuat skrip ini simpel sehingga kemudian _slackers_ menirunya untuk ribuan paket lainnya  di luar paket standar. Kumpulan _slackbuilds_ paket nonstandar itu disimpan di repo dengan alamat slackbuilds.org yang kemudian lebih sering disebut SBo. Oiya, paket nonstandar ini maksudnya adalah paket yang tidak ada di repo _official_ **slackware**. 

_Slackbuilds_ simpel karena

1. Berupa skrip. Skrip ini mempunyai keuntungan antara lain mudah diedit, konsumsi RAM kecil untuk mengedit, dan bisa diedit dengan editor teks apa saja.
2. Sebagai _template_. Umumnya _software_ tidak ada perubahan cara menginstal. Ini membuat semakin mudah. Ada peningkatan versi, maka tinggal ganti bagian `VERSION`, selesai.

Lalu, apa yang ditulis di _slackbuilds_? _Slackbuilds_ biasanya mempunyai susunan :

1. _Shebang_ sebagai penanda bahwa skrip ini dieksekusi dengan `bash`
2. Identitas _software_ atau paket, meliputi informasi nama, versi, dan _build_ ke berapa. _Slackers_ memberikan tambahan _tags_ sebagai penanda bahwa itu adalah paket yang dibuat komunitas atau dirinya. _Tags_ antara lain SBo, alien, willysr, wls, dll.
3. Penentuan arsitektur dan _build flags_
4. Ekstraksi kode sumber dari arsip
5. _Patching_ atau penyesuaian kode sumber jika diperlukan
6. Kompilasi
7. Penanganan dokumentasi
8. _Packing_ paket biner yang biasanya berekstensi txz atau tgz