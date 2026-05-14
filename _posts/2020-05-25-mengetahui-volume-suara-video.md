---
date: 2020-05-25
title: Mengetahui volume suara video
categories: [multimedia]
tags: [audio, ffmpeg]
---
Sebelum menggabung-gabungkan beberapa video menjadi 1, penting untuk mengetahui berapa intensitas suara/volumenya, agar beberapa video itu bisa diatur sedemikian rupa sehingga suaranya seragam volumenya atau hampir sama dari awal sampai akhir.

Untuk mengetahui intensitas suara video intro.mkv

```shell
ffmpeg -i intro.mkv -filter:a volumedetect -f null /dev/null
Input #0, matroska,webm, from 'intro.mkv':
  Metadata:
    COMPATIBLE_BRANDS: isommp42
    COM.ANDROID.VERSION: 9
    MAJOR_BRAND     : mp42
    MINOR_VERSION   : 0
    ENCODER         : Lavf58.29.100
  Duration: 00:00:14.90, start: 0.000000, bitrate: 5559 kb/s
    Stream #0:0(eng): Video: mpeg4 (Simple Profile), yuv420p, 3840x2160 [SAR 1:1 DAR 16:9], 30 fps, 30 tbr, 1k tbn, 30 tbc (default)
    Metadata:
      HANDLER_NAME    : VideoHandle
      ENCODER         : Lavc58.54.100 mpeg4
      DURATION        : 00:00:14.900000000
    Stream #0:1(eng): Audio: vorbis, 48000 Hz, stereo, fltp (default)
    Metadata:
      HANDLER_NAME    : SoundHandle
      ENCODER         : Lavc58.54.100 libvorbis
      DURATION        : 00:00:14.849000000
Stream mapping:
  Stream #0:0 -> #0:0 (mpeg4 (native) -> wrapped_avframe (native))
  Stream #0:1 -> #0:1 (vorbis (native) -> pcm_s16le (native))
Press [q] to stop, [?] for help
Output #0, null, to '/dev/null':
  Metadata:
    COMPATIBLE_BRANDS: isommp42
    COM.ANDROID.VERSION: 9
    MAJOR_BRAND     : mp42
    MINOR_VERSION   : 0
    encoder         : Lavf58.29.100
    Stream #0:0(eng): Video: wrapped_avframe, yuv420p, 3840x2160 [SAR 1:1 DAR 16:9], q=2-31, 200 kb/s, 30 fps, 30 tbn, 30 tbc (default)
    Metadata:
      HANDLER_NAME    : VideoHandle
      DURATION        : 00:00:14.900000000
      encoder         : Lavc58.54.100 wrapped_avframe
    Stream #0:1(eng): Audio: pcm_s16le, 48000 Hz, stereo, s16, 1536 kb/s (default)
    Metadata:
      HANDLER_NAME    : SoundHandle
      DURATION        : 00:00:14.849000000
      encoder         : Lavc58.54.100 pcm_s16le
frame=  447 fps= 97 q=-0.0 Lsize=N/A time=00:00:14.90 bitrate=N/A speed=3.24x    
video:234kB audio:2784kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown
[Parsed_volumedetect_0 @ 0x1a28300] n_samples: 1425280
[Parsed_volumedetect_0 @ 0x1a28300] mean_volume: -12.1 dB
[Parsed_volumedetect_0 @ 0x1a28300] max_volume: 0.0 dB
[Parsed_volumedetect_0 @ 0x1a28300] histogram_0db: 10593
```

Dari hasil tersebut di atas, tampak bahwa rata-rata intensitas suara/volumenya -12,1 dB dengan maksimum 0,0 dB. 
