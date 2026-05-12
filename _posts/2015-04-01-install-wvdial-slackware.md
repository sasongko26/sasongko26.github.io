---
date: 2015-04-01
title: Install wvdial slackware
categories: [jaringan]
tags: [wvdial]
---
Agar bisa internetan di Slackware dengan modem tentunya kita harus install dulu paket atau aplikasinya. Aplikasi yang penulis sarankan adalah WvDial. WvDial ini berbasis text/CLI, bisa untuk GSM maupun CDMA. Slackware yang digunakan Slackware 14.1.

Paket yang dibutuhkan:

- WvStreams
- WvDial

Kita akan unduh dari sini

WvStreams :

- Slackbuild : <http://slackbuilds.org/slackbuilds/14.1/libraries/wvstreams.tar.gz>
- Source code : <http://wvstreams.googlecode.com/files/wvstreams-4.6.1.tar.gz>

WvDial :

- Slackbuild : <http://slackbuilds.org/slackbuilds/14.1/network/wvdial.tar.gz>
- Source code : [http://slackbuilds.org/slackbuilds/14.1/network/wvdial.tar.gz](http://wvstreams.googlecode.com/files/wvdial-1.61.tar.gz)

Kemudian masuk ke /usr/local/src

```shell
cd /usr/local/src
```

Kemudian salin slackbuild wvstream dan wvdial ke direktori ini (/usr/local/src).

Yang harus diinstall dahulu adalah wvstreams. Ekstrak slackbuild wvstream

```shell
tar -xzf wvstreams.tar.gz
```

Akan muncul direktori wvstreams pindahlah ke direktori ini. Salin source code wvstreams ke direktori wvstreams kemudian ekstrak di direktori ini

```shell
tar -xzf wvstreams-4.6.1.tar.gz
```

Setelah itu, beri slackbuildnya hak eksekusi dan jalankan slackbuildnya

```shell
chmod +x wvstreams.SlackBuild && ./wvstream.SlackBuild
```

Kemudian akan terbuat file installer wvstreams-4.6.1-i486-1_SBo.tgz di /tmp. Nama file ini mungkin tidak sama untuk Anda, silahkan disesuaikan, kalau arsitektur komputer yang Anda gunakan 64 bit maka i486 ganti X86_64.

```shell
installpkg /tmp/wvstreams-4.6.1-i486-1_SBo.tgz
```

Install wvstreams selesai. Sekarang lanjut install wvdial. Caranya sama seperti install wvstreams. Yaitu:

Scanning your serial ports for a modem.

```shell
Modem Port Scan\<\*1\>: S0 S1 S2 S3\
ttyUSB0\<\*1\>: ATQ0 V1 E1 – OK ttyUSB0\<\*1\>: ATQ0 V1 E1 Z – OK ttyUSB0\<\*1\>: ATQ0 V1 E1 S0=0 – OK ttyUSB0\<\*1\>: ATQ0 V1 E1 S0=0 &C1 – OK ttyUSB0\<\*1\>: ATQ0 V1 E1 S0=0 &C1 &D2 – OK ttyUSB0\<\*1\>: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 – OK ttyUSB0\<\*1\>: Modem Identifier: ATI – Manufacturer: huawei ttyUSB0\<\*1\>: Speed 9600: AT – OK ttyUSB0\<\*1\>: Max speed is 9600; that should be safe. ttyUSB0\<\*1\>: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 – OK ttyUSB1\<\*1\>: ATQ0 V1 E1 – failed with 2400 baud, next try: 9600 baud ttyUSB1\<\*1\>: ATQ0 V1 E1 – failed with 9600 baud, next try: 9600 baud ttyUSB1\<\*1\>: ATQ0 V1 E1 – and failed too at 115200, giving up. ttyUSB2\<\*1\>: ATQ0 V1 E1 – OK ttyUSB2\<\*1\>: ATQ0 V1 E1 Z – OK ttyUSB2\<\*1\>: ATQ0 V1 E1 S0=0 – OK ttyUSB2\<\*1\>: ATQ0 V1 E1 S0=0 &C1 – OK ttyUSB2\<\*1\>: ATQ0 V1 E1 S0=0 &C1 &D2 – OK ttyUSB2\<\*1\>: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 – OK ttyUSB2\<\*1\>: Modem Identifier: ATI – Model: E1550 ttyUSB2\<\*1\>: Speed 9600: AT – OK ttyUSB2\<\*1\>: Max speed is 9600; that should be safe. ttyUSB2\<\*1\>: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 – OK

Found a modem on /dev/ttyUSB0. Modem configuration written to /etc/wvdial.conf. ttyUSB0: Speed 9600; init “ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0” ttyUSB2: Speed 9600; init “ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0”
```

Kemudian kita atur file konfigurasinya di /etc/wvdial.conf

```shell
[Dialer Defaults] Init1 = ATZ Init2 = ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 Modem = /dev/ttyUSB0 Phone = 0 Idle Seconds = 300 Modem Type = Analog Modem Stupid Mode = 1 Compuserve = 0 Baud = 9600 Auto DNS = 1 Dial Command = ATDT Ask Password = 0 ISDN = 0 ; Password = ; Username =
```

Berikut ini adalah konfigurasi wvdial penulis dengan ISP 3 modem Huawei E1550.

```shell
[Dialer Defaults] Init1 = ATZ Init2 = ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 Modem = /dev/ttyUSB0 Phone = 0 Idle Seconds = 300 Modem Type = Analog Modem Stupid Mode = 1 Compuserve = 0 Baud = 9600 Auto DNS = 1 Dial Command = ATDT Ask Password = 0 ISDN = 0 ; Password = ; Username =

[Dialer 3data] Init1 = ATZ Init2 = ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 Init3 = AT+CGDCONT=1,“IP”,“3data” Modem = /dev/ttyUSB0 Phone = 0 Idle Seconds = 300 Modem Type = USB Modem Stupid Mode = 1 Compuserve = 0 Baud = 9600 Auto DNS = 1 Dial Command = ATDT Ask Password = 0 ISDN = 0 Password = 3data Username = 3data New PPPD = yes Phone = *99*\*\*1#
```

Untuk menjalankannya

```shell
wvdial 3data
```
Nah, kalau keluar output seperti ini berarti sudah ada tanda-tanda konek.

```shell
WvDial: Internet dialer version 1.61
Initializing modem.
Sending: ATZ ATZ OK
Sending: ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 ATQ0 V1 E1 S0=0 &C1 &D2 +FCLASS=0 OK
Sending: AT+CGDCONT=1,“IP”,“3data” AT+CGDCONT=1,“IP”,“3data” OK
Modem initialized.
Idle Seconds = 300, disabling automatic reconnect.
Sending: ATDT*99*1#
Waiting for carrier. ATDT*99***1# CONNECT
Carrier detected.
Starting PPP immediately.
Starting pppd at Sun Apr 19 10:09:14 2015
Pid of pppd: 1669
Using interface ppp0
pppd: [08]pk·[17]F p[18]F
pppd: [08]pk·[17]F p[18]F
pppd: [08]pk·[17]F p[18]F
pppd: [08]pk·[17]F p[18]F pppd: [08]pk·[17]F p[18]F
pppd: [08]pk·[17]F p[18]F local IP address 10.107.213.208
pppd: [08]pk·[17]F p[18]F
remote IP address 10.64.64.64
pppd: [08]pk·[17]F p[18]F
primary DNS address 10.0.27.2
pppd: [08]pk·[17]F p[18]F
secondary DNS address 10.0.28.66
pppd: [08]pk·[17]F p[18]F
```
Loh kok disebut tanda-tanda konek? Kan di situ udah jelas ada tulisan **CONNECT** ,... ya karena ternyata

```shell
ping google.com
ping: unknown host google.com
```
buat nge-ping aja gagal apalagi browsing!

Oke, kalau terjadi seperti itu, salin aja /etc/ppp/resolv.conf ke /etc/resolv.conf
```shell
cp /etc/ppp/resolv.conf /etc/resolv.conf
```

Coba ping lagi

```shell
ping google.com
PING google.com (114.4.42.88) 56(84) bytes of data. 64 bytes
from 114.4.42.88: icmp_seq=1 ttl=58 time=1018 ms 64 bytes
from 114.4.42.88: icmp_seq=2 ttl=58 time=1209 ms 64 bytes
from 114.4.42.88: icmp_seq=3 ttl=58 time=369 ms 64 bytes
from 114.4.42.88: icmp_seq=4 ttl=58 time=689 ms 64 bytes
from 114.4.42.88: icmp_seq=5 ttl=58 time=371 ms
```
