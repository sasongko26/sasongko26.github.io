---
date: 2019-06-09
title: Backup data HP android
categories: [android]
---
Sebelum berganti ponsel atau HP sangat disarankan untuk mem-*back up* data-data penting, seperti dokumen, foto, video, maupun chat *WhatsApp*. Berikut cara menyalin file dari HP android ke laptop yang tentu saja laptopnya bersistem operasi **Slackware**.

# Persiapan **Slackware**

Pastikan bisa menjalankan `adb` yang merupakan bagian dari _android tools_. Kalau belum bisa install dari SBo

# Mengapa adb?

Mengapa adb? Mengapa tidak pakai *file manager* saja? Karena transfer pakai adb bisa lebih cepat

# Persiapan **Android**

Aktifkan mode **USB debugging** yang ada di *Settings* –\> *Developer options*. Apabila tidak ada bagian *Developer options* aktifkan dulu dengan cara *Settings* –\> *About phone*. Tekan beberapa kali *Build number* sampai muncul keterangan yang kurang lebih seperti ini “You are now a developer”. Jangan lupa konfirmasi izin akses perangkat. Pada HP tertentu mungkin akan diminta memasukkan IMEI terlebih dahulu sebagai *password* untuk mengakses *Developer options*. Dan, ingat-ingat lokasi penyimpanan file datanya. Dalam catatan kali ini ada di penyimpanan/memory internal (bukan memory external) di folder pindah.

# Next

Sambungkan kedua perangkat. Dari laptop kita gunakan adb

Pastikan perangkat telah siap digunakan. Cek apakah androidnya sudah siap

```shell
adb devices
List of devices attached
9H75BEO7W4UORSKF  device
```
Ok. Siap.

Kita pindahkan datanya ke *current working directory*

```shell
adb pull /storage/emulated/0/pindah/ .
```
Tunggu sampai selesai