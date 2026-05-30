---
date: 2017-07-05
title: Convert word ke pdf secara massal
categories: [manajemen  file]
tags: [libreoffice writer]
---
LibreOffice sudah lama mendukung konversi file dari Word/Writer (doc, docx dan odt) ke file pdf. Keunggulannya adalah bisa melakukan konversi secara massal.

Misalkan, dipunyai 1000 file docx yang tersimpan di \~/Documents. Masing-masing file ini akan dikonversi menjadi pdf di \~/convert.

```shell
soffice --headless --nologo --convert-to pdf:writer_pdf_Export --outdir ~/convert Documents/*.docx
```
Opsi –headless –nologo diberikan agar lebih cepat, lebih hemat waktu, karena tidak menampilkan *splash screen*.
