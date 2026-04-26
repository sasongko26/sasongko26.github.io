---
date: 2026-04-19
title: Mengenal pkgtool
categories: [manajemen paket]
tags: [pkgtool]
---
_Open source software (OSS)_ diadakan salah satunya untuk memudahkan hidup. **Slackware** pun demikian. Patrick J Volkerding, pengembang **slackware** memberikan kebebasan kepada _slackers_ untuk memilih manajer paket yang akan digunakan. **Slackware** mempunyai 2 manajer paket, yaitu `slackpkg` dan `pkgtool`. Pengenalan `slackpkg` sudah ada di [catatan sebelumnya]({% post_url 2026-04-18-mengenal-slackpkg %}).

`pkgtool` berbeda dengan `slackpkg`. Penggunaan `pkgtool` tidak bergantung ke internet. Berbeda dengan `slackpkg` yang untuk _update, install, upgrade_ memerlukan koneksi internet. File yang dikerjakan oleh `pkgtool` berada di lokal (pc/laptop pengguna) bukan server atau repo/_mirror_.

![pkgtool](assets/images/catatan-sasongko-pkgtool.png "Catatan Sasongko - pkgtool")

Fitur `pkgtool` antara lain

1. Install paket dari direktori aktif saat ini
2. Install paket dari direktori lain
3. Menghapus paket yang diinstall
4. Melihat isi paket
5. Menjalankan lagi skrip pemasangan **slackware**

