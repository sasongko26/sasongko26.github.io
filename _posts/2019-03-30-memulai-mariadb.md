---
date: 2019-03-30
title: Memulai mariadb
categories: [database]
tags: [mariadb]
---
# Apa itu MariaDB

MariaDB adalah *software* untuk manajemen basis data atau database. Merupakan pengembangan dari MySQL karena pada tahun 2010 MysSQL diakuisisi oleh Oracle.

# Install MariaDB

Secara *default*, apabila Slackware diinstall *full system* maka MariaDB akan terinstall. Jadi tidak usah repot-repot untuk installnya.

# Memulai MariaDB

Pertama setelah install jalankan sebagai root:

```shell
mariadb-install-db
```

Kemudian ubah kepemilikan direktori dan file di dalamnya menjadi milik mysql.
```shell
chown mysql:mysql -R /var/lib/mysql
```

Jalankan  ini kalau ingin service mariadb langsung aktif saat _booting_

```shell
chmod +x /etc/rc.d/rc.mysqld 
```

Selanjutnya perlu mengatur password atau kata sandi akun root dari database mariadb agar untuk masuk mariadb kita menggunakan user yang biasa kita pakai sehari-hari bukan root. Ini hanya opsional. Kita bisa masuk root database mariadb dengan akun root sistem.

```shell
mariadb-admin -u root password
```

Masuk ke root database

```shell
mariadb -u root -p
```

Selanjutnya silakan berdatabase ria.