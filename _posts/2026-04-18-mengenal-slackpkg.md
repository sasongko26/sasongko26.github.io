---
date: 2026-04-18
title: Mengenal slackpkg
categories: [manajemen paket]
tags: [slackpkg]
---
**Slackpkg** adalah alat manajemen paket otomatis yang dimiliki **slackware**. Slackpkg meng-_handle_ paket standar atau _official_ dari repo **slackware**. Otomasi di sini meliputi _install, uninstall_, dan _upgrade_. Tidak ada _dependency resolve_ otomatis. Akun _root_ dan koneksi jaringan internet dibutuhkan untuk menjalankan `slackpkg`.

# Pilih _mirror_

Sebelum menggunakan `slackpkg`, _slackers_ (pengguna **slackware**) harus memilih _mirror_ repo dahulu. File konfigurasi _mirror_ `/etc/slackpkg/mirrors`. Ada 2 tipe: _stable_ yang pada saat catatan ini ditulis merujuk ke angka 15.0 dan _current_. Pilih 1 saja. 15.0 atau _current_. Cara memilihnya adalah menghapus tanda `#` di baris _mirror_ terpilih. Hanya bisa memilih 1 baris. Pemilihan _mirror_ ini dilakukan biasanya 1x saja. Jika tidak ada keinginan beralih dari _stable_ ke _current_ atau sebaliknya, maka tidak perlu ganti. Jika _mirror_ terpilih ternyata lambat atau bahkan tidak aktif, sangat disarankan ganti _mirror_.

# Konfigurasi slackpkg

File konfigurasi utama slackpkg adalah `/etc/slackpkg/slackpkg.conf`. Mengapa konfigurasi utama? Karena ada konfigurasi lainnya di direktori yang sama, yaitu konfigurasi _mirror_, paket yang di-_blacklist_ dan _template_. Selain itu ada juga sampel konfigurasi setelah _install/upgrade_ paket tertentu. Sampel ini adalah file `post-functions.conf-sample`. Konfigurasi `slackpkg` insyaallah akan dibahas di catatan berikutnya. Saat ini biarkan dengan _default_.

# _Syntax_ slackpkg

`slackpkg` memiliki _syntax_

```shell
slackpkg [OPTIONS] <action> {PATTERN|FILE}
```

Apa maksud _syntax_ tersebut?

`slackpkg` : _script_ atau program yang dijalankan, yaitu slackpkg.

`[OPTIONS]`: konfigurasi yang bersifat opsional. Berada di dalam kurung siku `[]` menandakan bahwa opsi yang diberikan bisa 1 atau lebih. Opsi yang diberikan langsung dituliskan tanpa berada di dalam tanda kurung. Jika opsi ini dikosongkan, sistem akan menggunakan opsi _default_ yang ada di file konfigurasi utama.

`<action>`: aksi yang dilakukan. Hanya 1 aksi setiap menjalankan `slackpkg`. Ada beberapa aksi:

1. `help`. Menjalankan `slackpkg help` akan menghasilkan output teks panduan penggunaan `slackpkg`.
2. `update`. Perintah `slackpkg update` dijalankan untuk memeriksa apakah ada _update_ ada pembaruan di repo, dengan cara mendownload secara otomatis daftar paket terbaru. Sangat disarankan untuk `slackpkg update gpg` terlebih dahulu baru `slackpkg update` apabila install **slackware** pertama kali. Untuk pembaruan berikutnya `slackpkg update`.
3. `check-updates`. Jika sekedar ingin tahu apakah ada pembaruan, _slackers_ cukup menjalankan `slackpkg check-updates` untuk mengecek apakah perlu melakukan `slackpkg update` atau tidak. Jika tidak ada pembaruan maka tidak perlu _update_.
4. `show-changelog`. Gunakan `slackpkg show-changelog` untuk memeriksa lebih lenjut pembaruan apa yang tersedia. Perintah ini akan menampilkan file _ChangeLog.txt_ yang berisi informasi kapan pembaruan repo tersedia, paket yang berubah dan perubahannya apa (_upgraded, added, removed, rebulit_).
5. `search`. Untuk mencari paket dan statusnya gunakan `slackpkg search`.
6. `file-search`. Perintah `slackpkg file-search` lebih spesifik pencarian nama file (biasanya _library).
7. `install`. Menginstall paket di **slackware** yang ada di repo resmi gunakan `slackpkg install`.
8 . `upgrade`. Jika suatu paket di _ChangeLog.txt_ berstatus _Upgraded_, jalankan `slackpkg upgrade` untuk meng-_upgrade_ paket tersebut.
9. `reinstall`. Karena suatu hal paket yang diinstall ternyata korup. Intsall ulang paket tersebut adalah solusi. Jalankan `slackpkg reinstall` untuk install ulang paket korup.
10. `remove`. Bisa jadi _slackers_ tidak membutuhkan paket tertentu. Gunakan `slackpkg remove` untuk menghapus paket itu.
11. `download`. **Slackware** melalui **slackpkg** menyediakan ~paylater~ _install later_. Unduh file biner paketnya dengan `slackpkg download` kemudian install nanti.
12. `clean-system`. Jika ingin mengembalikan **slackware** ke paket standar, jalankan `slackpkg clean-system` untuk _uninstall_ semua paket nonstandar yang diinstall.
13. `upgrade-all` adalah versi massal dari `slackpkg upgrade`.
14. `install-new` digunakan untuk menginstall paket baru yang belum diinstall.
15. `new-config` digunakan untuk mengatur ulang konfigurasi file setelah install atau _upgrade_.
16. `generate-template` untuk membuat _template_ paket berdasarkan paket terinstall.
17. `install-template` melakukan installasi berdasarkan _template_ paket.
18. `remove-template` digunakan untuk _uninstall_ paket berdasarkan _template_.

Bagian akhir dari _syntax_ `slackpkg` adalah `{PATTERN|FILE}`. KUrung kurawal `{}` menunjukkan ini bisa jamak atau hanya 1. `PATTERN|FILE` artinya bisa berupa _pattern_ atau pola berupa _regex_ bisa juga file atau nama paket.

Penjelasan lebih lanjut penggunaan `slackpkg` insyaallah dibahas di catatan berikutnya.