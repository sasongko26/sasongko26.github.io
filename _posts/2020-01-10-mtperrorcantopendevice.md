---
date: 2020-01-10
title: Mtp error cant opendevice
categories: [manajemen file, android, hardware]
tags: [mtp, jmtpfs]
---
Ketika akan memindahkan data dari HP android ke laptop melalui thunar, menunggu lama dan berujung gagal. Setelah dicek dengan mencoba melalui jmtpfs

```shell
jmtpfs
Device 0 (VID=0e8d and PID=201d) is a MediaTek Inc Elephone P8000.
error returned by libusb_claim_interface() = -6LIBMTP PANIC: Unable to initialize device
terminate called after throwing an instance of 'MtpErrorCantOpenDevice'
  what():  Can't open device
Aborted
```
Ada masalah di libusb. Coba reinstall libusb

```shell
slackpkg reinstall libusb
```
Alhamdulillah sukses.
