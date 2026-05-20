---
date: 2020-05-14
title: Edit volume suara
categories: [multimedia]
tags: [ffmpeg]
---
*Editing* kali ini adalah bagaimana mengubah volume default audio/suara menggunakan **ffmpeg**. Misal, file yang akan diinput/diedit adalah video.mp4. Karena suaranya terlalu pelan, akan dinaikkan menjadi 5x semula melalui filter audio. File hasil editan diberi nama video-louder.webm.

```shell
ffmpeg -i video.mp4 -filter:a "volume=5" video-louder.webm
```

Apabila suara terlalu nyaring bisa dipelankan. Berikut akan dipelankan menjadi setengahnya dari volume semula dan file baru diberi nama new.webm

```shell
ffmpeg -i video.mp4 -filter:a "volume=0.5" new.webm
```

Atau, dengan menuliskan volume suaranya secara langsung. Default aslinya 256. Misalkan akan dinaikkan menjadi 300 kemudian disimpan sebagai anyar.mkv

```shell
ffmpeg -i video.mp4 -vol 300 anyar.mkv
```

Atau, bila dari mp4 kemudian tetap menjadi mp4 dan dengan kualitas video yang tidak jauh berbeda, dan untuk suara/audionya menggunakan codec opus (karena default mp4 codec audionya aac yang merupakan paten) nilai crf bisa diubah antara 0 - 51. 0 kualitas terbaik dengan konsekwensi ukuran lebih besar. Biasanya crf 17 bisa dikatakan aman, tidak terlalu tampak penurunan kualitasnya.

```shell
ffmpeg -i video.mp4 -af "volume=25.1dB" -acodec opus -strict -2 -vcodec copy -crf 17 video-suaranya-keras.mp4
```
