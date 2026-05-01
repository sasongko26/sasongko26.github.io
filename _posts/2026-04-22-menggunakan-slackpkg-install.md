---
date: 2026-04-22
title: Menggunakan slackpkg install
categories: [manajemen paket]
tags: [slackpkg]
---
**Slackpkg** adalah salah satu manajer paket yang dimiliki **slackware**. Ada banyak fitur yang disediakan, salah satunya adalah install paket. Fitur lainnya kami catat secara singkat [di sini]({% post_url 2026-04-18-mengenal-slackpkg %}).

_Software_ atau paket yang bisa diinstal dengan `slackpkg` hanyalah yang termasuk paket standar atau _official_ dari **slackware**. Paket lainnya bisa diinstall dengan [**pkgtool**]({% post_url 2026-04-19-mengenal-pkgtool %}) atau [_slackbuilds_]({% post_url 2026-04-20-mengenal-slackbuild %}).

_Syntax_-nya sederhana. Jalankan dengan _privilege_ **root**:
```bash
slackpkg install {PATTERN|FILE}
```

`{PATTERN|FILE}` menunjukkan bahwa bagian ini bisa lebih dari 1 karena menggunakan kurung kurawal, dan bisa berupa nama paket atau regex/pola nama paketnya.

Contoh, akan menginstall **emacs**, maka jalankan
```bash
slackpkg install emacs
```

Install berjama\'ah/lebih dari 1 paket, contoh **emacs** dan **qemu**
```bash
slackpkg install emacs qemu
```

Contoh install dengan nama paket yang memiliki pola tertentu, misalkan mengandung kata atau terkait _kernel_
```bash
slackpkg install kernel
```