---
date: 2026-08-03
title: Mengatur backlight dengan udev
categories: [hardware]
tags: [brightness]
---
Sekitar 4 tahun yang lalu kami pernah mencatat cara mengatur _brightness_ atau _backlight_. Berikut adalah lanjutan catatan tersebut sebagai alternatif atau tambahan. Kali ini kita menggunakan **udev**. Pengaturan ini membutuhkan _privelege_ **root**. Buat _rule_ dengan _path_/lokasi dan nama file /etc/udev/rules.d/81-intel-backlight.rules. Di sini kami menggunakan _intel backlight_ sesuai perangkat yang kami miliki. Nama file boleh juga dimodifikasi tidak harus sama persis dengan ini.

Isi dari file tersebut adalah:

```shell
# Set brightness to 1000 on boot for intel_backlight
SUBSYSTEM=="backlight", ACTION=="add", KERNEL=="intel_backlight", ATTR{brightness}="350"

# Optional: Ensure user in 'video' group can write to brightness file
SUBSYSTEM=="backlight", KERNEL=="intel_backlight", RUN+="/usr/bin/chgrp video /sys/class/backlight/intel_backlight/brightness"
SUBSYSTEM=="backlight", KERNEL=="intel_backlight", RUN+="/usr/bin/chmod g+w /sys/class/backlight/intel_backlight/brightness"
```
 Silakan isi <code>ATTR{brightness}="350"</code> dengan nilai yang diinginkan. Semakin tinggi semakin cerah.