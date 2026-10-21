---
date: 2024-10-22
title: Menjadikan docker aktif setelah boot
categories: [manajemen file]
tags: [docker]
---
Langkah selanjutnya setelah install **docker** adalah menentukan apakah **docker** akan dijalankan secara manual atau otomatis. Secara manual lebih efisien sumber daya karena benar-benar sesuai kebutuhan. Secara otomatis lebih memudahkan dan bisa lebih cepat eksekusi docker jika ada keperluan mendadak yang harus _as soon as possible_. **Docker** akan dijalankan secara manual atau otomatis, kuncinya harus _executable_ dulu.

```shell
chmod +x /etc/rc.d/rc.docker
```

Secara manual bisa diaktifkan dengan

```
/etc/rc.d/rc.docker start
```

Secara otomatis setelah _boot_ masukkan ini ke `/etc/rc.d/rc.local`

```shell
if [ -x /etc/rc.d/rc.docker ]; then
   /etc/rc.d/rc.docker start
fi
```

Selesai.