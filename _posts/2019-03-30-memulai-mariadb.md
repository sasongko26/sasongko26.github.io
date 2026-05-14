---
date: 2019-03-30
title: Memulai mariadb
categories: [database]
tags: [mariadb]
---
# Apa itu MariaDB

MariaDB adalah *software* untuk manajemen basis data atau database. Merupakan pengembangan dari MySQL karena pada tahun 2010 MysSQL diakuisisi oleh Oracle.

# Install MariaDB

Secara *default*, apabila Slackware diisnntall *full system* maka MariaDB akan terinstall. Jadi tidak usah repot-repot untuk insytallnya.

# Memulai MariaDB

```shell
mysql_install_db
chown -R mysql:mysql /var/lib/mysql
chmod +x /etc/rc.d/rc.mysqld # kalau ingin service mariadb langsung saat booting
mysqladmin -u root password # set password root
```

Untuk masuk ke mariadb

```shell
mysql -u [namauser]
```
