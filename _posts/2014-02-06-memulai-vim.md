---
date: 2014-02-06
title: Memulai vim
categories: [text editor]
tags: [vim]
---
Pengguna **linux** yang baru biasanya keder dengan **vim**. **Vim** memang kelihatan jadul dan seram di awal, tapi justru itu yang bikin dia cepat dan enak dipakai kalau sudah terbiasa. 

Untuk mulai pakai **vim**, gampang: buka **terminal**, lalu ketik

```shell
vim nama_file
```

Setelah itu akan dibawa oleh **vim** masuk ke **normal mode**, yaitu mode utama untuk navigasi dan perintah. Kalau mau mengetik, tekan `i` untuk masuk ke **insert mode**. Setelah selesai ketak-ketik, tekan `Esc` untuk balik lagi ke **normal mode**.

Beberapa perintah dasar yang wajib diingat:

1. `i` = mulai mengetik
2. `Esc` = keluar dari insert mode
3. `:w` = simpan file
4. `:q` = keluar
5. `:q! = keluar tanpa menyimpan
6. `:wq` = simpan lalu keluar
7. `dd` = hapus satu baris
8. `/kata` = cari teks

Kalau sering edit file konfigurasi, **vim** sangat berguna. Kuncinya cuma satu: biasakan pelan-pelan. Jangan hafal semua sekaligus. Mulai dari perintah dasar dulu, nanti lama-lama terbiasa terus seoleh-olah menjadi otomatis.