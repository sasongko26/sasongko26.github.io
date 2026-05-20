---
date: 2021-04-05
title: Transfer file dengan lftp
categories: [jaringan, manajemen file]
tags: [lftp]
---
Salah 1 akibat *Work from Home* a.k.a WfH adalah kapasitas *storage* laptop menjadi penuh. Semakin banyak file, semakin berkurang *free space*. Untuk menyiasatinya, ketika ada kesempatan bekerja di kantor, file-file tersebut ditransfer ke komputer kantor. Karena komputer kantor menggunakan **Windows 7** yang mana saya tidak paham bagaimana cara *file sharing*-nya saya gunakan ftp. Mungkin karena sudah terlanjur nyaman memakai **slackware**, saya tidak mau ribet pengaturan ftpnya di komputer kantor. Serahkan saja ke bagian IT untuk installnya. Pasrah sakbongkokan. Hahahaha….

Sebelum mulai menggunakan, pastikan *service* ftp windows berjalan.

```
net start ftpsvc
```

Oiya, ***Command* tersebut dijalankan di windows ya bukan slackware**. Kemudian, username komputer adalah akukamukita, dengan IP 192.168.120.47. Ok, login ke ftpnya dulu

<div class="highlight">

```shell
lftp akukamukita@192.168.120.47
Password: 
lftp akukamukita@192.168.120.47:~> 
```

Siap eksekusi! Karena akan memindahkan semua direktori lengkap dengan yang ada di *working directory*, gunakan mirror -R

```shell
lftp akukamukita@192.168.120.47:/> mirror -R
cd `.' [FEAT negotiation...]
```

Ups, datang feat negotiation menghadang.

```shell
lftp akukamukita@192.168.120.47:/> set ftp:use-feat false
```

Mari lanjutkan

```shell
lftp akukamukita@192.168.120.47:/> mirror -R
Total: 13 directories, 20 files, 0 symlinks                             
New: 20 files, 0 symlinks
2810640970 bytes transferred in 879 seconds (3.05 MiB/s)
```
Alhamdulillah done!
