---
date: 2024-09-28
title: Jalankan windows dari linux dengan qemu
categories: [virtualisasi]
tags: [qemu]
---
Sebagian masyarakat memilih untuk *dualboot* atau bahkan *multiboot* dalam berkomputer. Satu Perangkat komputer diinstall lebih dari satu sistem operasi. Alhasil, harddisk pasti terbagi menjadi paling sedikit 2 partisi. Tak jarang, sistem operasi tersebut adalah linux dan windows. Kelemahan dari model seperti ini adalah pengguna harus memilih salah satu, mana sistem yang akan dijalankan. Namun, tidak demikian bila ada qemu.

Qemu memungkinkan sistem operasi windows dipanggil atau dijalankan dari linux. Untuk dapat menjalankannya perlu install qemu (tentu saja) dan edk2-ovmf. Keduanya tersedia di SBo.

Misalkan linux dan windows terinstall di harddisk /dev/sda, menggunakan cpu sama seperti pada host dan dengan memori 6144 MB, maka windows bisa dijalankan dengan perintah:

```shell
qemu-system-x86_64 \
   --bios /usr/share/edk2-ovmf-x64/OVMF_CODE.fd \
   --enable-kvm \
   --cpu host \
   -m 6144 \
   -drive format=raw,file=/dev/sda
```
