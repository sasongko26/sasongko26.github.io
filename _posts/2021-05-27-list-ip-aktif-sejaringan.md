---
date: 2021-05-27
title: list IP aktif sejaringan
categories: [jaringan]
tags: [ip address]
---
Sebelum mengetahui alamat IP aktif dalam 1 jaringan yang sama, tentu saja harus konek atau masuk ke jaringan tersebut dulu. Setelah masuk, cek IP kita sendiri. Karena konek ke wifi maka _interface_-nya `wlan0`

```bash
ip addr show wlan0
```
dengan output

```bash
3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether cc:b0:da:b5:3b:75 brd ff:ff:ff:ff:ff:ff
    inet 192.168.43.20/24 brd 192.168.43.255 scope global dynamic noprefixroute wlan0
       valid_lft 1574sec preferred_lft 1574sec
    inet6 fe80::7f1b:2f4d:b98e:6500/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

Atau bisa juga dengan

```bash
nmcli
```
Dari *output* tersebut tampak bahwa ip lokal kita 192.168.43.20 dan _range_ ip 1-255. Maka untuk me-_list_ ip sejaringan yang aktif

``` bash
nmap -sn 192.168.43.1-255
```
dengan output
```bash
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-28 19:36 WIB
Nmap scan report for xkariote 192.168.43.1
Host is up (0.098s latency).
Nmap scan report for  (192.168.43.20)
Host is up (0.00033s latency).
Nmap done: 255 IP addresses (2 hosts up) scanned in 16.62 seconds
```

Dari *output* tersebut diketahui bahwa hanya 2 ip atau host yang aktif atau up, yaitu 192.168.43.1 dan 192.168.43.20. Tidak ada yang lain!
