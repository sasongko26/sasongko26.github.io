---
date: 2026-04-13
title: Slackware desktop
categories: [desktop]
tags: [window manager, desktop environment]
---
**Slackware** menyediakan beberapa _window manager_ (WM) dan _desktop environment_ (DE), yaitu:
1. TWM
2. MWM
3. Blackbox
4. Fluxbox
5. KDE Plasma
6. XFCE.

KDE Plasma berjalan dengan baik di lingkungan X11 maupun wayland. XFCE sudah mulai tersentuh wayland. Slackware juga memaketkan _wayland compositor_ **labwc**.

Pada saat instalasi terdapat pilihan untuk mengatur DE atau WM yang akan digunakan. KDE Plasma adalah pilihan _default_. Bagaimana jika setelah instal, _user_ ingin berganti DE atau WM? Mungkin karena sedang menginginkan variasi atau sekedar coba-coba. Ya, bisa saja. Tinggal ketikkan saja
```shell
xwmconfig
```
Akan keluar pilihannya. Klik `Ok` setelah selesai memilih. DE/WM pilihan bisa dijalankan dengan
```shell
startx
```

Jika menginginkan _wayland_ bisa
```shell
startkwayland
```
untuk menjalankan _KDE Plasma on Wayland_, atau
```shell
labwc
```
untuk menggunakan _wayland compositor_ labwc (_lab wayland compositor_).