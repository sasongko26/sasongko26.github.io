---
date: 2026-10-16
title: Menghapus user mariadb
categories: [database]
tags: [mariadb]
---
Dalam situasi tertentu, kita mungkin butuh untuk menghapus _user_ **mariadb**. Misalnya jika akun _user_ tersebut digunakan tidak sebagaimana mestinya. Bisa juga karena memang sudah tidak digunakan lagi akun maupun databasenya.

Cara menghapusnya, _login_ sebagai _root_ **mariadb**

```shell
mariadb -u root -p
```

Di _prompt_ **mariadb**

```sql
DROP USER nama_user;
```

Ganti `nama_user` dengan nama _user_/akun yang akan dihapus.

Selesai.