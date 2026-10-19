---
date: 2024-10-20
title: Install docker compose
categories: [virtualisasi]
tags: [docker]
---

**Docker compose** adalah alat yang memudahkan pengelolaan beberapa kontainer [Docker]({% post_url 2024-10-18-install-docker %}) sekaligus dalam satu proyek. Jika Docker biasa digunakan untuk menjalankan satu kontainer aplikasi, Docker Compose memungkinkan untuk menjalankan, mengatur, dan menghubungkan banyak kontainer sekaligus dengan satu perintah. Misalnya, jika aplikasi butuh database, server, dan cache, Docker Compose bisa mengelola semuanya secara bersamaan. Perbedaannya, Docker fokus pada satu kontainer, sedangkan Docker Compose mengatur kumpulan kontainer yang saling terhubung. Ini sangat membantu untuk pengembangan aplikasi kompleks tanpa harus menjalankan perintah Docker satu per satu. Dari sisi user ini juga memudahkan karena tidak perlu pusing kalau ada konflik dependensi atau lainnya.

Seperti dokcer, **docker compose** juga tersedia di [SBo]({% post_url 2026-04-26-mengenal-sbo %}). Sehingga untuk install bisa dengan
```shell
sboinstall docker-compose
```
Selesai