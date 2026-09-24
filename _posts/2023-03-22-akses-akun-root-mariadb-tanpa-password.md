---
date: 2023-03-22
title: Akses root mariadb tanpa password
categories: [database]
tags: [mariadb]
---

Untuk akses _root_ **mariadb** biasanya memerlukan _password_. Tapi sebenarnya _root_ bisa diakses tanpa _password_. Walaupun sebenarnya hal itu sangat berbahaya. Sangat tidak disarankan. Tapi jika menginginkannya bisa saja dilakukan. Pertama, hentikan dulu *service* **mariadb**-nya.

```shell
/etc/rc.d/rc.mysqld stop
```

Kemudian, _restart database server_ tanpa peduli otentikasinya.

```shell
mariadbd-safe --skip-grant-tables --skip-networking &
```

Nah, akun _root_ **mariadb** sudah bisa diakses tanpa *password*

```shell
$ mariadb -u root
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3
Server version: 10.11.2-MariaDB Source distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 
```

Oiya, 3 *command* pertama dijalankan dengan *privilege* **root** yang ada di sistem di mana **mariadb** tersebut diinstall.