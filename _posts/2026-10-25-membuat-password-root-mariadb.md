---
date: 2026-10-25
title: Membuat password root mariadb
categories: [database]
tags: [mariadb]
---
**Mariadb** memberikan kebebasan kepada penggunanya terkait penguasa tertinggi database alias akun root. Kebebasan tersebut bukanlah bebas sebebas-bebasnya, melainkan kebebasan yang bisa dipertanggungjawabkan. Apa maksudnya? Root sebagai pemegang kekuasaan tertinggi perlu diberikan batasan? Apa batasannya? Salah satunya adalah siapa yang bisa bertindak seperti root dan ini tidak lain tidak bukan, tentu saja akun root sistem.

Akun root sistem secara _default_ bisa masuk ke **mariadb**  tanpa _password_ sebegai penguasa tertingginya. Untuk meningkatkan keamanan, akun root **mariadb** bisa diberikan _password_. Begini caranya:

```shell
mariadb-admin -u root password
```
Akan muncul _prompt_ `New paassword:`

Silakan ketik _password_-nya. Kemudian untuk loginnya

```shell
mariadb -u root -p
```
Kemudian masukkan _passowrd-nya.

Selesai.