---
date: 2021-01-31
title: Membuat file csv
categories : [manajemen file, statistika, libreoffice]
tags: [csv, libreoffice calc]
---
File **csv** merupakan file yang umum digunakan sebagai file data. Mudah dalam pembuatannya. Begitu juga dengan aksesnya. Bisa dibuat dengan *text editor, spreadsheet software* maupun *statistical software*. Pada kesempatan kali ini tidak menggunakan *statistical software* seperti **R**.

# Membuat file csv dengan *text editor*

Prinsip pembuatan:

1.  Antar kolom dipisahkan oleh tanda koma (,)
2.  Baris pertama (umumnya) sebagai *header* atau nama/judul kolom
3.  Antar baris dipisahkan oleh enter
4.  Angka dituliskan seperti biasanya
5.  Teks/*string* dituliskan dalam tanda kutip

Contoh, data kasus malaria tahun 2019 terdiri atas 2 kolom, yaitu provinsi dan jumlah.

```shell
"Provinsi","Jumlah"
"Aceh",48
"Sumatera Utara",270
"Sumatera Barat",124
"Riau",26
"Jambi",142
"Sumatera Selatan",280
"Bengkulu",1454
"Lampung",502
```

Selanjutnya simpan dengan ekstensi **.csv**

# Membuat file csv dengan libre office calc

*Spreadsheet software* yang kami pilih adalah **libre office calc**. Langsung tuliskan datanya pada *workbook* atau *sheet*-nya. **Libre office calc** akan mengenali data secara otomatis apakah itu *number, date, currency* ataupun *string*. Jadi untuk penulisan teks tidak perlu menyertakan tanda kutip. Separator/pemisah antar kolom otomatis. Berpindah kolom bisa menggunakan tombol **tab** atau *arrow key left/right*. Berpindah baris bisa *arrow key up/down* atau enter. Setelah itu simpan dengan ekstensi **.csv** atau **filetype** : **Text CSV (.csv)**
