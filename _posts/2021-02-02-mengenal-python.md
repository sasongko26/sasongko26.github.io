---
date: 2021-02-02
title: Mengenal python
categories: [pemrograman]
tags: [python]
---

# Apa itu python

Python adalah bahasa pemrograman yang diciptakan oleh Guido van Rossum. Python bersifat *open source* sehingga semua orang boleh menggunakan dan mengembangkannya. Bahasa pemrograman satu ini tidak spesifik untuk keperluan tertentu, tetapi umum. Python bisa digunakan untuk membuat aplikasi desktop, database, web, *data science, machine learning*, dll.

# Apakah python cocok untuk data science? Mengapa?

Ya. Karena python *open source* maka semua orang boleh mengembangkannya, termasuk untuk keperluan *data science*. Contohnya adalah pembuatan *library* **numpy, scipy, pandas, scikit-learn, matplotlib, seaborn**, dll.

# Library untuk apakah itu?

1.  **Numpy** (*numerical python*) adalah library yang memudahkan dalam pendefinisian array baik dan juga memiliki fungsi-fungsi untuk aljabar linier.
2.  **Scipy** (*Scientific Python*) merupakan library yang ditujukan untuk keperluan komputasi saintifik seperti keperluan aljabar linier, integrasi dan diferensiasi numerik, transformasi Fourier, optimasi, interpolasi, statistik dan yang lainnya.
3.  **Pandas** (*Python data analysis*) adalah library untuk pengolahan data tabular untuk mengolah data dari file **CSV, TSV, Excel, SQL queries, Google BigQuery, SAS, Stata, SPSS**, dsb.
4.  **Matplotlib** digunakan untuk visualisasi dari data ke dalam bentuk grafik 2D atau 3D, seperti line chart, bar chart, histogram, polar chart, error bar plot.
5.  **Scikit-learn** adalah **Scipy Toolkit** yang ditujukan untuk menghasilkan model *predictive* dengan menggunakan *machine learning*.
6.  **Seaborn** merupakan library yang dibuat dari matplotlib yang ditujukan oleh visualisasi grafik statistik dengan warna yang menawan, terintegrasi dengan baik dengan **pandas**.

# Struktur bahasa python

1.  Statements.
2.  Variables
3.  Literals (nilai dari variable)
4.  Operators
5.  Reserved Words (tidak bisa digunakan sebagai variable, seperti True, return, for, whila)
6.  Whitespace (spasi, tab, python memperhatikan indentasi)
7.  Comments

# Bagaimana memulai python

Python adalah bahasa *scripting*. Secara default menggunakan *text based interface* atau *command line interface*. Python memiliki mode interaktif dan mode script. Mode interaktif menuliskan dan menjalankan kode baris-perbaris. Sedangkan mode script menuliskan keseluruhan kode ke dalam file berekstensi **.py** kemudian mengeksusi file tersebut.

Masuk ke mode interaktif, umumnya dengan menjalankan

```shell
$ python
Python 2.7.18 (default, Jan 20 2021, 22:57:02) 
[GCC 10.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

*Command* **python** yang akan dieksekusi dituliskan pada tempat setelah \>\>\>. Pada **slackware**, *command* tersebut akan menggunakan **python 2**. **Slackware current** secara *default* memberikan 2 versi **python** yaitu **python 2** dan **python 3**. Untuk menggunakan **python 3**

```shell
$ python3
Python 3.9.1 (default, Jan 20 2021, 22:58:54) 
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Untuk keluar dari mode interaktif tekan **Ctrl D**. Masuk ke mode script atau menjalankan script python

```shell
$ python namafile.py
```

# Di mana bisa belajar python dari nol dengan mudah

Banyak sumber belajar baik itu berupa *ebook*, video tutorial, artikel, blog maupun lembaga kursus seperti [**dqlab**](https://dqlab.id/signup?referralCode=SASO3950).