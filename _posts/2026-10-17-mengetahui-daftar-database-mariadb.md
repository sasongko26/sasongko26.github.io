---
date: 2026-10-17
title: Mengetahui daftar database mariadb
categories: [database]
tags: [mariadb]
---
Untuk mengetahui database apa saja yang dibuat dengan **mariadb** kita bisa login ke _user_ **mariadb** yang ingin diketahui databasenya.

```shell
mariadb -u nama_user -p
```

Ganti nama\_user dengan nama dari _user_ yang ingin diketahui databasenya. Kemudian di dalam _prompt_ **mariadb**

```sql
SHOW DATABASES;
```
akan muncul database apa yang ada di _user_ itu.

Selesai.