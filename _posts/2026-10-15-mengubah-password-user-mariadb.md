---
date: 2026-10-15
title: Mengubah password user mariadb
categories: [database]
tags: [mariadb]
---
_Password_ akun atau _user_ database **mariadb** yang sudah dibuat, seperti misalnya pada [catatan kemarin]({% post_url 2026-10-14-membuat-user-database-baru-mariadb %}), bisa diubah. Caranya, _login_ sebagai _root_ **mariadb**,
```shell
mariadb -u root -p
```

Sudah masuk ke _prompt_ **mariadb**. Jalankan

```sql
ALTER USER nama_user IDENTIFIED BY 'tulis_password_barunya_di_sini';
```

Ganti `nama_user` dengan nama _user_ yang diubah _passwordnya_ dan masukkan _password_ bari di `tulis_password_barunya_di_sini`.

Selesai.