---
date: 2023-06-22
title: Convert dd ke vdi
categories: [manajemen file, virtualisasi]
tags: [dd, virtualbox]
---
Untuk konversi file dd/img menjadi vdi mudah. Pastikan sudah install virtualbox. Misalkan akan mengubah file1.dd menjadi file2.vdi,

```shell
VBoxManage convertfromraw file1.dd --format VDI file2.vdi
```
