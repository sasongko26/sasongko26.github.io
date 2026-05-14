---
date: 2021-01-27
title: Pelengkap dnscrypt-proxy
categories: [jaringan]
tags: [dnscrypt]
---
Catatan ini merupakan catatan tambahan untuk melengkapi **README.Slackware** pada skrip **dnscrypt-proxy** yang ada di SBo. Yang ada di SBo :

1.  Membuat grup **dnscrypt** dan usernya
2.  Mengkonfigurasi dns **/etc/resolv.conf.head**
3.  Memasukkan **dnscryp-proxy** ke /etc/rc.d/rc.local{,\_shutdown}

Nah, berikut ini tambahannya. Mungkin tidak semuanya membutuhkan, jadi *maintainer* **dnscrypt-proxy** tidak mengikutsertakan langkah ini. Penulis menggunakan **NetworkManager**, setelah *check & recheck*, `dnscrypt-proxy` tidak bekerja karena file /etc/resolv.conf terkena *overwrite* oleh **NetworkManager**. Ini adalah langkah untuk memberikan imunisasi/mencegah *overwrite*. *Command* berikut dijalankan dengan *root privilege*

```shell
cp /etc/resolv.conf.head /etc/resolv.conf
chattr +i /etc/resolv.conf
```
