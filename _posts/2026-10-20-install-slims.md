---
date: 2026-10-20
title: Install slims
categories: [sistem informasi manajemen]
tags: [slims]
---
**Slims** adalah sistem perpustakaan digital yang dirancang untuk memudahkan pengelolaan dan akses koleksi buku serta sumber informasi lainnya. Dengan teknologi modern, **slims** memungkinkan perpustakaan di berbagai tempat untuk mengelola data buku, peminjaman, pengembalian, dan katalog secara efisien dan terintegrasi. Sistem ini juga mendukung pencarian cepat dan akurat, sehingga masyarakat dapat dengan mudah menemukan buku yang dibutuhkan.

**Slims** bersifat _open source_ sehingga bisa digunakan semua orang dan gratis. _Software_ ini tersedia untuk **linux** dan _windows_. Selain _open source_, aplikasi ini buatan dalam negeri lho. Dikembangkan oleh para pustakawan dan orang-orang yang berkecimpung di dunia perpustakaan.

Sayangnya **slims** belum tersedia di [SBo]({% post_url 2026-04-26-mengenal-sbo %}) apalagi _slackware official repo_. Sebenarnya pengembang menyediakan _source code_ **slims** di github. Kami coba install sesuai petunjuk di dokumentasinya ternyata _complicated_ jika diterapkan ke **slackware**. Maksudnya, membutuhkan _patch_ agar sesuai dengan pakem **slackware**. Nah, untuk membuat _patch_ ini yang kami belum sempat, atau lebih tepatnya _aras-arasen_ untuk menyempatkan diri di tengah cuaca Kota ATLAS yang panas ini. Walhasil, pakai [**docker**]({% post_url 2024-10-18-install-docker %}) saja yang biasanya tidak terlalu ribet. Berhubung ada file `docker-compose.yml` di reponya, sekalian saja [install **docker compose**]({% post_url 2024-10-20-install-docker-compose %}) kalau belum diinstall agar lebih mudah.

Setelah **docker compose** terinstall, pastikan **service docker** berjalan. 

```shell
ps aux|grep docker
```

Kalau hasilnya hanya `grep` berarti **docker** belum aktif. Jalankan

```shell
bash /etc/rc.d/rc.docker start
```

jika ingin docker langsung aktif setelah booting jangan lupa untuk menjadikannya _executable_ dengan
```shell
chmod +x /etc/rc.d/rc.docker
```

Kemudian, _download_ **slims**
```shell
git clone https://github.com/slims/slims9_bulian.git
```

Oiya, **Slims 9 Bulian** adalah release terbaru untuk saat ini.

Lalu masuk direktorinya dan lakukan pengaturan awal.
```shell
cd slims9_bulian
```

Pengaturan pertama adalah _environment_-nya.

```shell
cp .env.example .env
```

atur sesuai kebutuhan/kehendak. Berikut adalah file `.env.example`yang dimaksud 

```shell
HTTP_PORT=8881
DB_PORT=3307
APP_ENV=production
DB_USER=root
DB_PASS=your_db_password_here
DB_NAME=senayan
```
Bagian yang sering diubah adalah `DB_PASS`. Untuk mendapatkan detil terkait error ubah `APP_ENV` dari `production` ke `development`.

Langkah selanjutnya, jalankan

```shell
docker compose up -d --build
```

Tunggu sebentar sampai semua _services_ berstatus `started`. Kemudian buka di web browser `localhost:8881`. Jika halaman **slims** muncul berarti sudah selesai diinstall. Adapun untuk menjalankan tugas sebagai pustakawan silakan login dengan _url_  `localhost:8881/?p=login`.