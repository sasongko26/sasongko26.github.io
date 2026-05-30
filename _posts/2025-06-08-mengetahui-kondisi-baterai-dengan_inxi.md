---
date: 2025-06-08
title: Mengetahui kondisi baterai dengan inxi
categories: [hardware]
tags: [battery]
---
Beberapa tahun yang lalu kami pernah mencatat bagaimana cara mengetahui kondisi baterai melalui *command line* atau **terminal**. Saat itu kami gunakan **upower**. Sekarang, mari kita lengkapi catatan tersebut dengan *tool* lain, yaitu **inxi**.

Mengapa **inxi**? Karena *command*-nya lebih singkat daripada **upower**.

```shell
$ inxi -B
Battery:
  ID-1: BAT0 charge: 14.7 Wh (38.7%) condition: 38.0/38.0 Wh (100.0%)
```

*Output* tersebut menunjukkan bahwa jumlah baterai 1 ( hanya ada ID-1) dengan daya aktif 14.7 Wh atau 38.7%. Kondisi baterai sempurna karena kapasitasnya 100%.

Hasil tersebut masih bisa dilengkapi dengan menambahkan opsi x ataupun xx. Dengan penambahan opsi ini bisa diketahui juga apakah saat ini sedang dalam pengecasan atau tidak. Ini akan sangat berguna jika kita menggunakan *window manager* atau *compositor* yang tidak menampilkan info baterai.
