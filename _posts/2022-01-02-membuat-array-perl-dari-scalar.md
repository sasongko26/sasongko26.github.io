---
date: 2022-01-01
title: Membuat array perl dari scalar
categories: [pemrograman]
tags: [perl]
---
Array merupakan variabel pada **perl** dengan data yang nilainya majemuk. Sedangkan scalar bernilai tunggal. Catatan kali ini tentang bagaimana cara membuat array dari scalar yang tersedia.

```perl
my $nama = "Sasongko";
my $jenis_kelamin = "Laki-laki";
my $distro = "Slackware";
my $tahun = 2021;
```

Keempat scalar tersebut akan disatukan menjadi array @biodata.
```perl
my @biodata = ($nama, $jenis_kelamin, $distro, $tahun);
```
