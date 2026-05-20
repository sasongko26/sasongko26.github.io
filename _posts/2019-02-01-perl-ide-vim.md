---
date: 2019-02-01
title: Perl IDE dengan vim
categories: [pemrograman]
tags: [perl]
---
Reputasi **vim** sebagai **text editor** sudah teruji berpuluh tahun. Ternyata **Vim** juga memiliki *support* **plugin** untuk **perl**. Hal ini membuat **vim** bisa dijadikan sebagai **integrated development environment (IDE)** untuk **perl**.

*Download plugin*-nya kemudian extract
```shell
wget https://www.vim.org/scripts/download_script.php?src_id=24473 -O perl-support.zip -O perl-support.zip
mkdir -p .vim
unzip perl-support.zip -d .vim
```

Aktifkan

```shell
echo "filetype plugin on" >> .vimrc
```
