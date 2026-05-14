---
date: 2021-03-09
title: Mount partisi hibernated windows
categories: [manajemen file, hardware]
tags: [mount]
---
Lima tahun yang lalu ketika membeli laptop yang saat ini digunakan untuk menulis catatan ini, toko memberikan OS Windows 10 tanpa lisensinya. Penulis tetap mempertahankannya untuk jaga-jaga jika di kemudian hari kepepet sangat membutuhkan Windows.

Tadi pagi iseng ingin melihat-lihat adakah file di partisi tempat Windows diinstall yang bisa dihapus sehingga storage harddisk lebih lega?

Partisi Windows teridentifikasi sebagai /dev/sda2. Akan di-*mount* ke /media/hd0

```shell
mount /dev/sda2 /media/hd0
Windows is hibernated, refused to mount.
Falling back to read-only mount because the NTFS partition is in an
unsafe state. Please resume and shutdown Windows fully (no hibernation
or fast restarting.)
```

What? Windows is hibernate? Seingat penulis selalu tertib dalam menjalankan SOP shutdown (*close* semua window aplikasi yang terbuka, shutdown melalui menu, tidak ada *warning* apapun yang muncul di monitor). Jadi ya dianggap baik-baik saja. Ternyata tidak.

Kemudian coba difixkan

```shell
ntfsfix /dev/sda2
Mounting volume... Windows is hibernated, refused to mount.
FAILED
Attempting to correct errors... 
Processing $MFT and $MFTMirr...
Reading $MFT... OK
Reading $MFTMirr... OK
Comparing $MFTMirr to $MFT... OK
Processing of $MFT and $MFTMirr completed successfully.
Setting required flags on partition... OK
Going to empty the journal ($LogFile)... OK
Windows is hibernated, refused to mount.
Remount failed: Operation not permitted
```
Masih gagal ternyata. Ok, lanjut.

```shell
ntfs-3g -o remove_hiberfile /dev/sda2 /media/hd0
```

Alhamdulillah clear. Sudah ter-*mount* dengan baik.
