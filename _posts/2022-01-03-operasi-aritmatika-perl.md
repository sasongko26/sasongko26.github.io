---
date: 2022-01-03
tile: Operator aritmatika scalar perl
categories: [pemrograman]
tags: [perl]
---
Variabel scalar merupakan variabel tunggal dalam perl. Pada variabel ini bisa dilakukan beberapa operasi aritmatika seperti penjumlahan, pengurangan, perkalian, pembagian, modulus, pemangkatan, *autoincrement, autodecrement*.

Pada operasi aritnatika, dikenal bilangan bertipe integer dan float. Integer adalah bilangan bulat. Float bilangan desimal.

```perl
#!/usr/bin/perl

use strict;
use warnings;
use feature 'say';

my $a = 2;
my $b = 25;

say("Angka pertama (a) adalah $a");
say("Angka kedua (b) adalah $b");

# penjumlahan
my $c = $a + $b;
say("a+b = $c");

# pengurangan
my $d = $b - $a;
say("b-a = $d");

# perkalian
my $e = $a * $b;
say("a*b = $e");

# pembagian
my $f = $a / $b;
my $g = $b / $a;
say("a/b = $f");
say("b/a = $g");

# pemangkatan
my $h = $a ** $b;
my $i = $b ** $a;
say("a^b = $h");
say("b^a = $i");

# autoincrement
# tanda + di depan
say("Nilai a sebelum autoincrement = $a");
my $j = ++$a;
say("++a = $j");
say("Nilai a sesudah autoincrement = $a");

# tanda + di belakang
say("Nilai b sebelum autoincrement $b");
my $k = $b++;
say("$b++ = $k");
say("Nilai b setelah autoincrement $b");

# autodecrement
# tanda - di depan
say("c = a+b. c sebelum autodecrement = $c");
my $l = --$c;
say("l = c setelah autodecrement = $l");
# tanda - di belakang
my $m = $c--;
say("c setelah autodecrement = $m");

# modulus (sisa hasil bagi)
my $a = 3;
my $b = 30;
my $n = $a % $b;
my $o = $b % $a;
say("a = $a");
say("b = $b");
say("a%b = $n");
say("b%a = $o");
```

