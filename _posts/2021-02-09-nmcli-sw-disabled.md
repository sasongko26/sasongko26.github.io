---
date: 2021-02-09
title: nmcli sw disabled
categories: [jaringan]
tags: [nmcli]
---
Beberapa saat yang lalu penulis terkena *prank* dari diri sendiri. Sebut saja demikian karena awalnya hanya iseng mengaktifkan **flight mode** di laptop. Beberapa saat kemudian karena ada keperluan laptop dibiarkan begitu saja. Sewaktu menggunakan lagi, menyambungkan ke internet tidak bisa-bisa. Cek **nmcli**

```shell
nmcli
p2p-dev-wlan0: disconnected
        "p2p-dev-wlan0"
        wifi-p2p, sw disabled, hw

eth0: unavailable
        "Realtek RTL810xE"
        ethernet (r8169), C8:5B:76:66:51:6C, hw, mtu 1500

wlan0: unavailable
        "Qualcomm Atheros QCA9377"
        wifi (ath10k_pci), 8E:58:C9:8B:64:0F, sw disabled, hw, mtu 1500

lo: unmanaged
        "lo"
        loopback (unknown), 00:00:00:00:00:00, sw, mtu 65536

Use "nmcli device show" to get complete information about known devices and
"nmcli connection show" to get an overview on active connection profiles.

Consult nmcli(1) and nmcli-examples(7) manual pages for complete usage details.
```
Ada *output* yang aneh : **sw disabled**. Penulis baru ingat kalau **flight mode**-nya aktif. Setelah dinonaktifkan, semua kembali normal. **sw disabled** enyah dari *Output* **nmcli**.
