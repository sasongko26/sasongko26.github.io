---
date: 2023-06-27
title: Install guest os qemu
categories: [virtualisasi]
tags: [qemu]
---
Akan diinstall sebagai *guest os* slackware, dengan file iso slackware.iso, *disk image* slackware.qcow dan virtual RAM 5GB. Maka *command* yang dijalankan dengan qemu adalah

```shell
qemu-system-x86_64 -enable-kvm -m 5120 -cdrom slackware.iso -drive file=slackware.qcow2 -boot d
```

