---
date: 2021-02-01
title: Download video youtube khusus member
categories: [jaringan]
tags: [youtube-dl]
---
Secara *default* video yang ada di **youtube** dapat di-*download* secara bebas. Semua orang bisa men-*download* tanpa harus login. Tetapi, ada kalanya sang pemilik video membatasinya hanya untuk *member* atau harus login dulu baru bisa *donwload*.

Dengan **youtube-dl** hal ini mudah dilakukan

```shell
youtube-dl -u username url
```
Opsi -u diikuti dengan **username** akun *youtube* untuk login.
