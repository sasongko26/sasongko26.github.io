---
date: 2024-10-18
title: Install docker
categories: [virtualisasi]
tags: [docker]
---
**Docker** adalah salah satu _container_ yang saat ini naik daun. Kami gunakan **docker** untuk menjalankan aplikasi yang terasa sulit diinstall di **slackware** karena adanya konflik sistemik seperti perbedaan paket termasuk dependensinya. **Docker** tersedia di [SBo]({% post_url 2026-04-26-mengenal-sbo %}) sehingga bisa diinstall dengan menjalankan

```shell
sboinstall docker
````

Oiya, untuk _build_ **docker** membutuhkan **go**, sehingga sangat disarankan selama proses kompilasi menggunakan _login shell_ **root** dengan

```shell
su -
```

Selesai.