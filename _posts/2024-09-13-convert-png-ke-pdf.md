---
date: 2024-09-13
title: Convert png ke pdf
categories: [manajemen file]
tags: [mogrify, imagemagick]
---
Melengkapi catatan yang sudah ada tentang konversi file. Kali ini adalah konversi atau convert file dari berformat png menjadi pdf. Misalkan file gambar.png akan dikonversi menjadi pdf, maka *command*-nya

```shell
mogrify -format pdf gambar.png
```
*Command* tersebut di atas adalah bagian dari **imagemagick** yang secara default sudah terinstall di **slackware**.
