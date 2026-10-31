---
date: 2026-10-23
title: Membuat tampilan ncurses monokrom foot
categories: [terminal]
tags: [ncurses, foot]
---
Awalnya saya bingung catatan ini akan diberikan judul apa. Saya menggunakan **slackware** di lingkungan **wayland** dengan **terminal emulator**-nya aadalah **foot**. Saya _update_ dan _upgrade_ sistem biasanya 1 bulan 1x. Setiap kali menjalankan
```shell
slackpkg upgrade-all
```
muncul daftar paket atau _software_ yang bisa di-_upgrade_. Sayangnya saya tidak merasa cocok dengan pewarnaan yang ditampilkan. Pada pilihan atau list tersebut, tulisannya berwarna kungi, _background_ berwarna hijau. Warna ini secara bersama-sama membuat saya menjadi agak kesulitan untuk membacanya dengan jelas.

Agar lebih mudah dibaca, saya tambahkan di awal di depan sebelum menjalankan programnya
```shell
TERM=vt100
```
Warnanya menjadi hitam putih biasa yang lebih nyaman kami simak.

Jika ingin permanen setiap buka **foot** langsung aktif, maka tambahkan ke `~/.config/foot/foot.ini`

```
[main]
term=vt100
```
SSelesai.