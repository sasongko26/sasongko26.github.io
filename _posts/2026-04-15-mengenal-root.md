---
date: 2026-04-15
title: Mengenal root
categories: [manajemen user,manajemen file]
tags: [root,home]
---
# Urgensi mengenal root
Mengenal `root` sangat penting karena pembicaraan tentang `root` tidak hanya satu lingkup bahasan sesuai konteksnya. Ada beberapa konteks atau konsep tentang `root` ini. Kesalahan mengidentifikasi konteks bisa membuat _linuxer_ tidak mengerjakan apa-apa atau bahkan menghapus linux yang telah dia install.

# Root sebagai main directory
Konsep pertama: _**root as main directory**_. `Root` adalah direktori utama dari sistem _linux_ dan _BSD_ sekeluarga. Direktori ini dilambangkan dengan `/`. Semua direktori berada di bawah `/`. Contoh: `/bin` adalah direktori `bin` yang tepat berada di bawah `/`. `/usr/bin` adalah direktori `bin` yang di bawah `usr` dan direktori `usr` ini di bawah _main directory_ `/`.

# Root sebagai user
Konsep kedua: _**root as superuser**_. `Root` adalah _user_ dengan wewenang tertinggi, sehingga disebut sebagai _super user_. Wewenang tersebut meliputi _read, write, execute_ semua file. _Read_ membaca atau melihat isi suatu file atau direktori. _Write_ secara bahasa adalah menulis, tetapi lingkup wewenang menulis ini termasuk memodifikasi, edit dan menghapus. _Execute_ mengeksekusi atau menjalankan suatu _script_ atau program biner. _Linuxer_ harus cermat saat menggunakan `root` dan tidak boleh sembarangan dalam memutuskan akan bertindak sebagai `root`.

# /root
Konsep berikutnya: `/root` adalah _home directory_ dari _user_ atau akun _root_. "Rumah" milik _root_. `/root` adalah direktori khusus, tidak ada user lain yang memiliki _home directory_ tepat di bawah `/`.

# Root directory
Literatur ataupun forum yang berkaitan dengan _open source software_ kadang menyebutkan istilah _root directory_. _Root directory_ yang dimaksud bisa merupakan `/` atau selainnya. Contoh penggunaan yang selain `/` : ada suatu file arsip sebut saja `mawar.tar.gz`. File `mawar.tar.gz` diekstrak di `/home` muncullah direktori `mawar`. Direktori mawar ini memiliki subdirektori `mawar1` dan `mawar2`. Ketika disebut _root directory_ `mawar` maka maksudnya adalah direktori `mawar` yang ada di dalam `/home` bukan di bawah `/`. 
