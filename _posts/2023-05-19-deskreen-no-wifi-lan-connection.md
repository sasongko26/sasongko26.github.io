---
date: 2023-05-19
title: Deskreen no wiFi and LAN connection
categories: [jaringan]
tags: [deskreen]
---
Buka-buka direktori lama, ternyata ada catatan yang belum dipublikasikan, salah satunya soal **deskreen**. Aplikasi ini kami gunakan untuk *share screen* ataupun presentasi dari laptop ke TV. Sebenarnya untuk menghubungkan laptop dan TV bisa menggunakan kabel HDMI, tapi karena kabelnya kurang panjang, TVnya banyak dan belum punya *HDMI splitter* maka terbersitlah untuk presentasi menggunakan jaringan wifi. *Duckduckgo* memberikan hasil bagaimana cara, salah satunya dengan **deskreen** ini.

Demi kepraktisan, kami *donwload* edisi **appimage**. Namun, setelah dieksekusi ada masalah, yaitu muncul *error box* yang menyatakan bahwa **No WiFi & LAN Connection** padahal koneksi internet sudah berjalan lancar, stabil dan kencang di laptop maupun TV.

Solusinya, yang kami dapatkan dari *github* **deskreen** adalah dengan menambahkan *path* untuk **iproute2**

```shell
PATH=/usr/sbin ./Deskreen*.AppImage
```