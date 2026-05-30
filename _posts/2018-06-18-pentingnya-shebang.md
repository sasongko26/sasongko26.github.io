---
date: 2018-06-18
title: Pentingnya Shebang
categories: [pemrograman]
tags: [bash, perl, python, r]
---
# Shebang itu apa?

Pengguna linux, BSD, ataupun mac yang terbiasa melihat *source code* sangat mungkin sudah tidak asing lagi dengan **shebang**. Ada yang menyebut shebang sebagai **sh bang**, **shabang**, **hashbang**, **hashpling**, dan **poundbang**. Shebang ini dituliskan di baris pertama, yakni diawali dengan \#!.

Contoh, untuk **perl** :

```
#!/usr/bin/perl
```

atau

```
#!/usr/bin/env perl
```

Sebagai pengguna linux khususnya **Slackware**, *user* akan merasakan betapa pentingnya shebang ini. Kepentingannya terkait fungsi shebang itu sendiri dan bagaimana *user* menjalankannya.

# Fungsi shebang<a href="#fungsi-shebang" class="anchor" hidden="" aria-hidden="true">#</a>

Shebang berfungsi untuk memberi tahu sistem (pada komputer), **interpreter** apa yang digunakan. Apakah shell? Kalau shell, mau pakai bash, csh, ksh, atau zsh? Apakah perl? Ataukah python? Ataukah ruby?

# Bagaimana menjalankannya

Ada 2 cara yang biasa dilakukan untuk menjalankan program :

- Menyertakan interpreternya di awal *command*

Contoh :

```shell
perl program.pl
```

- Tanpa menuliskan interpreternya

Contoh :

```shell
./program.pl
```

Cara ini mengharuskan programnya (program.pl) dijadikan *executable* terlebih dahulu, sehingga bisa dieksekusi/dijalankan tanpa harus menuliskan interpreternya, yaitu dengan cara

```shell
chmod +x program.pl
```
# Contoh kasus

Misalnya, ada sebuah program yang filenya bernama tes, yang isinya

```
$a = 5

print $a
```

Bagi orang yang sudah berpengalaman (terutama programmer) bisa saja dengan cepat menentukan bahasa atau interpreter apa yang digunakan. Tapi bagaimana dengan yang “jam terbang” *coding* nya masih baru? Atau yang awam seperti saya? Mungkin bingung dan akan coba-coba. Ya, coba-coba karena filenya tanpa ekstensi. Kalau ada ekstensinya kan bisa lebih mudah, langsung ketahuan.

- bash

```shell
$ bash tes
tes: line 1: =5: command not found
tes: line 3: print: command not found
```
- csh

```shell
$ csh tes
a: Undefined variable.
```

- ksh

```shell
$ ksh tes
tes: line 1: =5: not found
```
- zsh

```shell
$ zsh tes
tes:1: 5 not found
```
- perl

```shell
$ perl tes
syntax error at tes line 3, near "print"
Execution of tes aborted due to compilation errors.
```
- python

```shell
$ python tes
  File "tes", line 1
    $a=5
    ^
SyntaxError: invalid syntax
```
- ruby

```shell
$ ruby tes
5
```

Ternyata ruby!

Di sisi lain, mari kita anggap saja tidak mau ambil pusing ini interpreternya apa. Pakai cara kedua.

```shell
$ ./tes
./tes: line 1: =5: command not found
./tes: line 3: print: command not found
```

Waduh…. error!

Nah, tidak menuliskan shebang ternyata bisa menimbulkan masalah. Kalau begini, tentu saja kontraproduktif dengan tujuan dibuatnya program sebagai sarana *problem solving*/menyelesaikan masalah.
