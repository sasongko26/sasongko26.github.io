---
date: 2022-01-04
title: Penggabungan operator perl
categories: [pemrograman]
tags: [perl]
---
Penggabungan operator yang dimaksudkan di sini adalah menggabungkan = dan operator lainnya seperti penjumlahan, perkalian, pengurangan, dll. Penggabungan ini biasanya digunakan untuk memperbarui nilai suatu variabel. Contoh di sini adalah penggabungan dengan operator penjumlahan.

Misalkan, terdapat variabel a dengan nilai awal 10. Nilai a kemudian akan diubah dengan cara ditambah 4. Nilai a yang baru ini dituliskan dengan

```perl
a += 4;
```
Sehingga nilai a kemudian berubah dari 10 menjadi 14.
```perl
#!/usr/bin/perl

use strict;
use warnings;
use feature "say";

my $a = 10;
say("Nilai a awal. a = 10");
$a += 4;
say("Nilai a baru setelah ditambah 4. a += 4. a = $a");
```

