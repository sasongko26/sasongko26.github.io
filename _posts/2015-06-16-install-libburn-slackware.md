---
date: 2015-06-16
title: Install libburn
categories: [manajemen paket]
tags: [libburn]

Libburn adalah pustaka (*library*) untuk menulis ke CD, DVD, dan *blueray*.

Berikut langkah-langkah installnya di slackware melalui slackbuild. Adapun versi libburn yang diinstall adalah 1.4.0.

Pertama, pastikan [tersambung internet]({% post_url 2015-04-01-install-wvdial-slackware %}) untuk mengunduh paket. Kemudian unduh slackbuild libburn.

```shell
wget http://slackbuilds.org/slackbuilds/14.1/libraries/libburn.tar.gz
```

Ekstrak

```shell
tar xzf libburn.tar.gz
```

Akan terbentuk folder libburn. Pindah direktori ke folder itu.

```shell
cd libburn
```

Kemudian unduh kode sumber libburn.

```
wget http://files.libburnia-project.org/releases/libburn-1.4.0.tar.gz
```

Install slackbuildnya

```
sh libburn.SlackBuild
```

Install paketnya

```
installpkg /tmp/libburn-1.4.0-x86_64-1_SBo.tgz
``