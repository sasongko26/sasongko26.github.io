---
date: 2020-05-05
title: Trimming video ffmpeg
categories: [multimedia]
tags: [ffmpeg]
---
Misalkan, kita akan mencuplik sebagian (*trimming*) video video-asli.mp4 dari menit ke 57 lebih 34 detik sampai durasi ke 1 jam 2 menit 5 detik. Fila hasil *trimming* adalah cuplikan.mp4

```shell
ffmpeg -i video-asli.mp4 -ss 00:57:34 -to 01:02:05 -c copy cuplikan.mp4
```
