---
date: 2021-11-28
title: Variabel array perl
categories: [pemrograman]
tags: [perl]
---
Melanjutkan catatan sebelumnya tentang variabel yang dimiliki bahasa pemrograman **perl**. Sebelumnya membahas tentang variabel **scalar**. Catatan kali ini tentang jenis variabel yang kedua yaitu **array**.

Berbeda dengan **scalar** yang bernilai tunggal, **array** bernilai majemuk. Array merupakan himpunan. Element **array** *zero indexed*, artinya, elemen pertama berindeks 0.

Pendeklarasian array diserta simbol @.

Contoh: himpunan nama-nama buah dan daftar nilai

```perl
my @buah = ("pisang", "mangga", "jeruk", "pepaya");
my @daftar_nilai = (80, 100, 76.5, 21.87);
```
Tampilkan 
```perl
print $buah[0];
```
menghasilkan output pisang. Sedangkan

```perl
print $daftar_nilai[2];
```
menghasilkan output 76.5.
