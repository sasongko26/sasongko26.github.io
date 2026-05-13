---
date: 2022-11-16
title: Mengatur brightness
categories: [desktop,hardware]
tags: [brightness]
---
Pengaturan *brightness* bisa dilakukan dengan melakukan *assign* nilai pada

```shell
/sys/class/backlight/intel_backlight/brightness
```

Adapun nilai maksimal yang bisa diset ada di

```shell
/sys/class/backlight/intel_backlight/max_brightness
```
Oiya, di atas menggunakan *graphics* **intel** jadi *intel_backlight*.
