---
date: 2021-09-10
title: Install QGIS via flatpak
categories: [manajemen paket]
tags: [flatpak, qgis]
---
**QGIS** adalah aplikasi sistem informasi geografis populer dan mudah digunakan. **QGIS** sudah ada di **SBo**, tetapi *build*-nya lama. Jadi saya install via **flatpak** saja.

```shell
flatpak install --from  https://flathub.org/repo/appstream/org.qgis.qgis.flatpakref
```

Untuk menjalankannya, bisa klik dari menu atau jalankan

```shell
flatpak run org.qgis.qgis
```

Untuk meng-*update* jalankan

```shell
flatpak update
```
