---
date: 2026-04-11
title: Login slackware tty
categories: [manajemen user, keamanan]
tags: [login]
---
**Slackware** mempertahankan _command line interface_ (CLI) yang berbasis teks. Komputer dinyalakan kemudian _booting_ sampai _login_. Semua itu dengan tampilan teks. Ujung bawah dijumpai _login prompt_ seperti ini:
```shell
Welcome to Linux 6.18.18 (tty1)
darkstar login:
```

"Sambutan" `Welcome to` diikuti dengan `Linux`, `6.18.18', dan `(tty1)`.  `Linux` adalah nama kernel yang aktif, `6.18.18` aalah versi kernel, dan `(tty1)` menunjukkan _teletypewriter_ yang aktif.

Baris berikutnya, `darkstar` adalah _hostname_ yang dituliskan saat install. Kemudian _login prompt_ `login:`. Kursor otomatis ditempatkan di sebelah kanan _login prompt_ ini. Masukkan _username_ kemudian `enter`.

Kemudian muncul `password:' dan masukkan _password_-nya. Loh, kok kosong? Tidak ada tulisan yang terlihat, entah itu huruf, angka, ataupun asterisk layaknya kalau menuliskan _password_! _Keyboard_ tidak berfungsi? Install lancar tapi mengapa _login_ jadi kacau begini?

Pengguna baru, atau yang mencoba sebelum membaca-baca dokumentasi, mungkin akan panik. Inilah yang kami alami saat pertama kali menggunakan **slackware**. Sebelumnya kami memakai **BlankOn** dan di kantor (sama seperti kantor pada umumnya) _Microsoft Windows_ yang tampilannya grafis. Pindah **slackware** jadi _njegleg_ dalam bahasa Jawa. Orang Inggris menyebutnya _jetlag_.

Tenang.... Ini normal. Mode CLI memang sengaja tidak menampilkan _password_ yang diketik. Tujuannya? Biar lebih aman. Kok bisa?

Bayangkan ketika kita sedang login, mengetikkan _username_ dan _passsword_, di belakang kita ada yang mengintip. **Slackware** yang dalam hal ini mewakili **linux** dan sistem operasi _open source_ lainnya, yaitu **BSD** seperti **OpenBSD** dan **FreeBSD** yang login dengan antarmuka berbasis teks memang _secure by default_. Sudah _by design_ seperti itu. Jika _password_ yang diketik ditampilkan apa adanya, bisa ditebak kan? Lalu, mengapa kosong, tidak disensor saja misalnya dengan digantikan karakter asterisk atau bintang? Ketika _password_ yang dituliskan diganti dengan asterisk atau karakter lainnya, berarti membuka celah keamanan. Pengintip bisa mengetahui berapa panjang _password_. Pengintip bisa mengira-ngira _password_ bahkan bisa juga _brute force_ yang lebih sistematis sehingga menambah risiko akun diambil alih.

Lalu, bagaimana cara loginnya kalau seperti itu? Ya langsung ketik saja _password_-nya kemudian `enter`. Apa yang tidak terlihat bukan berarti tidak ada. _Password_ ada, diketik, tapi tidak ditampilkan demi keamanan.

Kalau login sukses akan tampil _user prompt_ `#` untuk _root_ atau `$` untuk _user_ lainnya. Kalau gagal, muncul _login prompt_ lagi.

