---
date: 2015-12-26
title: Tidak ada ikon NetworkManager di panel
categories: [desktop]
tags: [xfce]
---
Iseng-iseng install lagi slackware tapi tanpa paket yang ada di kategori *ap* atau direktori slackware/ap dan *xap* (slackware64/xap).

Efek sampingnya adalah, tidak adanya ikon NetworkManager di panel. Di sini saya gunakan DE XFCE. Sementara itu paket direktori slackware/n semuanya terinstall.

Install dulu appletnya. Karena saya punya berkas ISOnya maka installnya bisa offline asalkan tahu di mana letak paketnya berada. Setelah mount ISOnya ke /mnt/iso,

```shell
installpkg /mnt/iso/slackware64/xap/network-manager*.txz
```

Ketika memunculkan ikon/applet NetworkManagernya ke panel,

```shell
nm-applet
nm-applet: error while loading shared libraries: libsqlite3.so.0: cannot open shared object file: No such file or directory
```

Libsqlite3.so.0 gagal dibuka karena tidak ada filenya. File ini ada kalau install sqlite3.

```shell
installpkg /mnt/iso/slackware64/ap/sqlite-3*.txz
```

Setelah paket sqlite3 terinstall yang berarti libsqlite3.so.0 sudah bisa dibuka nm-applet, ternyata masih ada masalah.

```shell
nm-applet

** (nm-applet:1223): WARNING **: Could not initialize NMClient /org/freedesktop/NetworkManager: The name org.freedesktop.NetworkManager was not provided by any .service files
** Message: applet now removed from the notification area
** Message: applet now embedded in the notification area
** Message: applet now removed from the notification area

** (nm-applet:1223): WARNING **: Failed to register as an agent: (2) The name org.freedesktop.NetworkManager was not provided by any .service files
```

NetworkManager tidak berjalan. Maka harus kita jalankan dulu pakai root.

```shell
NetworkManager
```

Nah, NetworkManager sudah jalan, selanjutnya jalankan nm-applet lagi dan lempar ke *background* maka ikon NetworkManager muncul di panel.

```shell
$ nm-applet &
```
