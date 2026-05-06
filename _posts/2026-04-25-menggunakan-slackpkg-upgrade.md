---
date: 2026-04-25
title: Menggunakan slackpkg upgrade
categories: [manajemen paket]
tags: [slackpkg]
---
`slackpkg upgrade` mungkin termasuk 10 besar _command_ yang sering dijalankan _slackers_. Penggunaannya mirip dengan `slackpkg install`. Dengan perintah ini paket yang terinstall akan disamakan versinya dengan yang ada di repo. _Command_ ini bisa dijalankan untuk 1 paket atau lebih, sesuai kebutuhan ataupun selera.

Syntaxnya adalah
```bash
slackpkg upgrade {PATTERN|FILE}
```

Contoh, untuk upgrade _kernel generic_,
```bash
slackpkg upgrade kernel-generic
```

Untuk upgrade vim, gvim dan emacs
```bash
slackpkg upgrade vim, gvim, emacs
```

Jika ingin upgrade semua paket yang memungkinkan diupgrade.
```bash
slackpkg upgrade-all
```