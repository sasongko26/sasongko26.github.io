---
date: 2022-05-26
title: Sinkronisasi official repo
categories: [manajemen paket]
tags: [slackpkg]
---
*Package management* atas *packages* yang ada di *official repo* pda **slackware** dapat dilakukan dengan dengan **slackpkg**. Sinkronisasi perlu dilakukan agar *packages* yang diinstall merupakan versi terbaru sesuai yang disediakan di repo. Sinkronisasi ini meliputi 2 kegiatan, yaitu sinkronisasi *database packages* dan versi *packages*.

Sinkronisasi *database packages* meliputi *list* apa saja file yang ada di repo, checksum, dll. Dilakukan dengan

```shell
slackpkg update
```

Khusus untuk versi *packages*, menyamakan versi terinstall dengan versi repo untuk semua *packages*

```shell
slackpkg upgrade-all
```

atau apabila hanya ingin *upgrade* tertentu saja contohnya **kernel**

```shell
slackpkg upgrade kernel
```
Untuk memilih *packages* apa yang diinstall dapat menggunakan spacebar. Jangan lupa pilih OK untuk meng-_upgrade_,