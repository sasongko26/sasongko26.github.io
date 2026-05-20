---
date: 2022-02-23
title: Disable fortune postlogin
categories: [login]
tags: [fortune]
---
Secara *default*, setelah berhasil *login* di **tty** muncul pesan-pesan berupa kata-kata mutiara dari para tokoh. **Fortune** ini menjadi sepaket dengan **bsd-games**. Jadi kalau ingin di-*disable* bisa uninstall **bsd-games**. Kalau masih butuh **bsd-games** tinggal jadikan file /etc/profile.d/bsd-games-login-fortune.\*sh *nonexecutable*

```shell
chmod -x /etc/profile.d/bsd-games-login-fortune.*sh
```
