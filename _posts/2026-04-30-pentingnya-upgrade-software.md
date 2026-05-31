---
date: 2026-04-30
title: Pentingnya update software
categories: [promosi]
tags: [keamanan]
---
Salah satu manfaat yang kami dapatkan ketika menggunakan _open source software_ adalah menjadi tercerahkan. Salah satunya menjadi sadar bahwa _upgrade software_ itu penting. _Update_ pada judul ini yang kami maksud adalah _upgrade_. __Upgrade_ yang dimaksud adalah menaikkan versi _software_ yang terinstall sehingga sama dengan versi terbaru (atau versi tertentu) yang disediakan pengembangnya. Misal: versi **python** terinstall adalah 3.11.1, versi terbaru dari repo 3.12.13. Sedangkan _update_ adalah memperbarui **metadata** atau catatan terkait _software_ itu seperti nama dan versinya.

Rilis baru tidak lepas dari hal berikut:

1. Perbaikan _bug_
2. Penambalan celah keamanan
3. Penambahan/penghapusan fitur

_Upgrade_ menjadi penting, bahkan sangat penting dan sesegera mungkin harus dilakukan jika  terkait dengan masalah keamanan.

Contoh: ditemukan celah keamanan berupa _local privilege escalation_ pada suatu software. _Proof of Concept_ (PoC) berupa file yang ditulis dengan bahasa pemrograman python dengan nama `celah-keamanan.py`. Nama file ini sudah kami modifikasi, karena sebagai gambaran saja. Untuk detil tanpa sensor bisa japri. File tersebut jika dijalankan dengan _user_ biasa akan bisa mengakses perintah yang seharusnya hanya bisa diajalankan oleh **root**. Mudahnya adalah, dengan menjalankan file tersebut, _user_ biasa menjadi **root** tanpa _password_!

```shell
$ python celah-keamanan.py && su
#
```
Pada baris 1, ada 3 perintah:

1. `python celah-keamanan.py`: menjalankan _script_ untuk membobol keamanan tersebut.
2. `&&`: untuk melanjutkan menjalankan perintah berikutnya.
3. `su`: perintah untuk _switch user_ yang secara _default_ berganti ke **root**. Normalnya _user_ akan diminta untuk menuliskan _password_ akun **root**.

Baris 1 tersebut menggunakan _user prompt_ alias dijalankan oleh _user_. Normalnya _user prompt_ itu konsisten. Selama tidak berganti level, -user_ biasa tetap `$`. Perhatikan baris berikutnya. _Prompt_-nya menjadi `#` yang artinya telah berganti menjadi **root**. Hal ini kemudian bisa diverifikasi dengan menjalankan perintah yang memang wewenang dari **root** seperti `mount` , `ip` atau `blkid`.