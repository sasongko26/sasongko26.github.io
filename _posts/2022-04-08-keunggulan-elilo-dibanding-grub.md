---
date: 2022-04-08
title: Kenggulan elilo dibanding grub
categories: [boot loader]
tags: [elilo, grub]
---
Pascamigrasi dari **elilo** ke **grub** ada hal yang dirindukan. **Zram** dengan kompresi **zstd**. Entah masalahnya di mana, **zstd** tidak bisa digunakan untuk zram apabila menggunakan **grub**. Menggunakan **elilo** aman damai sentosa lancar jaya. Padahal **kernel** dan **initrd**-nya sama.

Untungnya, algoritma kompresi lainnya bisa digunakan, yaitu secara default **lzo-rle**. Alhamdulillah. Dengan adanya **zram** aktivitas komputasi di laptop dengan RAM hanya 2GB masih bisa dijalankan dengan lancar.
