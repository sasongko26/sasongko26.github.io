---
date: 2015-06-07
title: Install jdk slackware
categories: [manajemen paket]
tags: [jdk]
---
*Java Development Kit* atau yang biasa disingkat JDK ini berguna untuk membuat/mengembangkan aplikasi berbasis Java. Selain itu, untuk menginstall dan/atau menjalankan aplikasi tertentu disyaratkan JDK, seperti *LibreOffice*, *Netbeans* dan *Aptana*. Sebelum install kita unduh dulu dari http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html .

Karena *Slackware* yang digunakan adalah 64 bit maka pilih untuk yang LInux x64 format rpm. Untuk bisa mengunduh harus menyetujui perjanjian lisensi dulu (*Accept License Agreement*). Kemudian pindahkan hasil unduhan ke /usr/local/src dilanjutkan dengan pindah ke direktori /usr/local/src

```shell
rpm2tgz jdk-8u45-linux-x64.rpm
installpkg /usr/local/src/jdk-8u45-linux-x64.tgz
```

JDK sukses terinstall.
