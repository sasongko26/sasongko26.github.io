---
date: 2026-04-14
title: Membuat user baru
categories: [manajemen user]
tags: [pembuatan akun user]
---
**Slackware** secara _default_ menyediakan 1 _user_ yaitu _root_. _User_ ini mempunyai kewenangan yang tinggi. Ahli _security_ dan _sysadmin_ merekomendasikan tidak menggunakan akun _root_ untuk pekerjaan yang tidak terkait pembuatan atau pemeliharaan sistem operasi. Jika komputer digunakan untuk membuat atau edit dokumen, memutar video atau lagu, _web browsing_, dll sudah seharusnya menggunakan akun _user_ biasa bukan _root_.

Untuk membuat akun _user_ baru, jalankan sebagai _root_
```shell
adduser
```
akan muncul _wizard_ atau panduan untuk menuliskan nama _user_, UID, grup, dsb.
