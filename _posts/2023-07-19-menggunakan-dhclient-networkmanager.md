---
date: 2023-07-19
title: Menggunakan dhclient untuk NetworkManager
categories: [jaringan]
tags: [dhclient, networkmanager]
---
Ada sedikit masalah ketika menggunakan kernel 6.1.38. Masalah tersebut antara lain tidak stabilnya jaringan internet bila konek via NetworkManager, usb dan bluetooth yang kadang suka diskonek sendiri. Solusi untuk masalah jaringan dan bluetooth tersebut adalah mengganti dhcpcd dengan dhclient pada konfigurasi Network Manager /etc/NetworkManager/conf.d/00-dhcp-client.conf, sesuai masukan dari Pak Walesa.
