---
date: 2021-02-26
title: Menghapus file berdasarkan pencarian
categories: [manajemen file]
tags: [find]
---
Misalkan akan menghapus semua file berekstensi **.rtf** di direktori /tmp. Pada direktori /tmp terdapat banyak direktori dan file lainnya. File yang akan dihapus hanya pada direktor induk, tidak termasuk subdirektorinya (maxdepth=1).

```shell
find /tmp -maxdepth 1 -name *.rtf -delete
```
