---
date: 2026-04-28
title: Install sbotools
categories: [manajemen paket]
tags: [sbotools]
---
**sbotools** adalah salah satu manajer paket yang menangani paket-paket dari [SBo]({% post_url 2026-04-26-mengenal-sbo %}). Cara installnya mudah.

1. _Download slackbuild_. Pakai _slackbuild_ yang disediakan lebih praktis.

```bash
curl -O https://slackbuilds.org/slackbuilds/15.0/system/sbotools.tar.gz
```

2. Ekstrak
```bash
tar xf sbotools.tar.gz
```

3. Masuk ke direktori hasil ekstraknya
```bash
cd sbotools
```

4. _Download_ kode sumber **sbotools**. Saat catatan ini ditulis versi terbaru adalah 4.1.4
```bash
curl -O https://pghvlaans.github.io/sbotools/downloads/sbotools-4.1.4.tar.gz
```

5. Berganti _user_ sebagai **root**
```bash
su
```

6. Jalankan _slackbuild_.
```bash
. sbotools.SlackBuild
```

7. Install file biner tgz hasil _build_. File ini ditampilkan lengkap nama dan lokasinya di akhir output eksekusi _slackbuild_.
```text
Slackware package /tmp/sbotools-4.1.4-noarch-1_SBo.tgz created.
```
Filenya adalah `/tmp/sbotools-4.1.4-noarch-1_SBo.tgz`.

8. Install
```bash
installpkg /tmp/sbotools-4.1.4-noarch-1_SBo.tgz
```

9. Opsional, tapi sangat dianjurkan jika sudah install versi lama dari sbotools (versi 2.9.3). Memperbarui konfigurasi _default_ agar bisa berjalan di **slackware** 15.0 dan -_current_.
```bash
slackpkg new-config
```
Kemudian pilih O untuk memakai konfigurasi baru.

Selesai, **sbotools** terinstall.
