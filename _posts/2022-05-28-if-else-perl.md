---
date: 2022-05-28
title: If else perl
categories: [pemrograman]
tags: [perl]
---
Penyeleksian kondisi di **perl** dapat menggunakan *syntax* if…else dengan format

```perl
if ( kondisi ) {
  ....
  } else {
  ....
  }
```


Contoh

```perl
#!/usr/bin/perl

use strict;
use warnings;
use feature 'say';

my $username = "user";
if ( $username eq "nama" ) {
    say "Oke";
    } else {
    say "Ulangi lagi....";
    }
```

