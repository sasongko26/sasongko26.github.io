---
date: 2026-09-23
title: Build emacs wayland
categories: [text editor]
tags: [emacs, wayland]
---
_Slackers_ pecinta **emacs** dalam lingkungan **wayland** sangat disarankan untuk menggunakan **emacs** dengan **pgtk**. Sayangnya, secara _default_ **emacs** yang disediakan **slackware** tidak dikompilasi dengan _pgtk_. Namun demikian, **emacs** di **wayland** sebenarnya masih bisa berjalan tetapi kurang maksimal. Sehingga sangat disarankan untuk melakukan _build_ sendiri.

Caranya mudah. Pertama. Melakukan  _build_ membutuhkan _source code_. Kami  memakai **rsync**. Sebelum melakukannya, buat dulu direktori tempat _source code_ akan disimpan, misalnya <code>emacs-pgtk</code>.

```shell
mkdir emacs-pgtk
```

Kemudian masuk ke direktorinya
```shell
cd emacs-pgtk
```

Ambil _source code_

```shell
rsync -av --progress rsync://slackware.nl/mirrors/slackware/slackware64-current/source/e/emacs/ ./
```

Setelah itu, mulai _build_ yang membutuhkan kewenangan _root_. Bisa berganti _user_ ke _root_ atau memakai **sudo**.

```shell
su
```

kemudian _build_ dengan mengaktifkan **pgtk**. 

```shell
PGTK_OPTION="--with-pgtk" ./emacs.SlackBuild
```

Tunggu beberapa saat sampai selesai _build_. Install file hasil _build_, contoh di sini /tmp/emacs-31.1-x86_64-2_pgtk.txz 

```shell
upgradepkg --reinstall --install-new /tmp/emacs-31.1-x86_64-2_pgtk.txz
```

Selesai.