---
date: 2026-05-09
title: Install imv
categories: [image viewer]
tags: [imv]
---
**imv** adalah _image viewer_ ringan yang dirancang untuk lingkungan linux modern, khususnya Wayland. Dibandingkan aplikasi penampil gambar lain, **imv** punya tampilan sederhana dan waktu _loading_ yang cepat. Aplikasi ini cocok untuk kita yang ingin melihat gambar tanpa harus berhadapan dengan banyak menu, panel, atau fitur yang jarang dipakai.

Salah satu keunggulan **imv** adalah dukungannya terhadap Wayland. Di desktop yang menggunakan Wayland, **imv** bisa berjalan secara _native_ tanpa harus bergantung pada kompatibilitas X11. Hasilnya, pengalaman melihat gambar terasa lebih menyatu dengan sistem, mulai dari respons saat membuka gambar, berpindah antarfile, sampai menampilkan gambar dalam mode _fullscreen_.

Pengoperasiannya juga praktis karena banyak mengandalkan _keyboard_. Kita berpindah ke gambar berikutnya, kembali ke gambar sebelumnya, memperbesar tampilan, atau menyesuaikan jendela tanpa perlu sering menyentuh _mouse_. Buat pengguna yang terbiasa minim klak-klik, cara seperti ini terasa cepat dan efisien.

_Slackers_ tidak perlu khawatir akan kesulitan menginstallnya. **imv** tersedia di [SBo]({% post_url 2026-04-26-mengenal-sbo %}). Sehingga install **imv** bisa dengan

```shell
sboinstall imv
```

Selesai.
