---
date: 2021-02-11
title: Copy paste xterm
categories: [terminal]
tags: [xterm]
---

**xterm** adalah **X terminal emulator** populer legendaris. Penulis masih menggunakannya sebagai terminal utama ketika menggunakan **blackbox**. Sesekali saat menggunakan **xfce** atau **kde**.

**xterm** ini khas. Tidak seperti **xfce4-terminal** atau **konsole** yang secara *default* pengguna bisa melakukan *copy paste* (Copas) dengan mudah. **Ctrl Shift C, Ctrl Shift V** untuk copas pada terminal emulator lainnya tidak berlaku! Butuh pengaturan khusus untuk melakukannya. Mengatur agar setiap yang diblok akan dimasukkan ke *clipboard*.

Untuk bisa melakukan *copy*:

```shell
echo "xterm*selectToClipboard : true" >> ~/.Xresources
```

Karena ~/.Xresources ada perubahan, agar bisa segera diterapkan tanpa *reboot*

```shell
xrdb -merge ~/.Xresources
```

Selanjutnya, untuk melakukan *copy* tinggal blok saja teks yang akan di-*copy*. Kemudian, *paste*-nya tekan **Shift Insert**.