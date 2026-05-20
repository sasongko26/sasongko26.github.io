---
date: 2018-05-08
title: Uninstall manual semua modul perl
categories: [pemrograman]
tags: [perl]
---
Cara *uninstall* semua modul perl yang dulunya *install* dari [CPAN](https://cpan.org) secara manual :

```shell
rm -r /usr/local/{lib{,64},share}/perl5
```

