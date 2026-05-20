---
date: 2022-01-05
title: Operator penggabungan pengulangan string perl
categories: [pemrograman]
tags: [perl]
---
Pada **perl**, variabel **scalar** yang berupa **string** dapat dilakukan penggabungan dan pengulangan. Contoh, terdapat 3 variabel sebagai berikut: \$sapa = “Hai…. " \$distro = “Slackware” \$penilaian = “distro terbaik.” Ketiga variabel tersebut akan digabungkan. Kemudian di baris selanjutnya,penampilan variabel \$distro akan diulang 5x. Untuk penggabungan digunakan “.”, sedangkan pengulangan dengan “x”.

```shell
#!/usr/bin/perl

use strict;
use warnings;
use feature "say";

my $sapa = "Hai.... ";
my $distro = "Slackware ";
my $penilaian = "distro terbaik.";

# penggabungan
say($sapa.$distro.$penilaian);

# pengulangan
say("$distro" x 5);
```

