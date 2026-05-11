---
date: 2016-07-03
title: Upgrade slackware 14\.2
categories: [manajemen paket]
---
Sehubungan dengan telah rilisnya **Slackware 14.2** maka silahkan melakukan *upgrade* untuk mendapatkan keamanan yang lebih bagus dan fitur-fitur baru. Saya selama ini melakukan ***upgrade* bertahap demi penghematan kuota internet**. Dimulai dengan upgrade ke *current* karena saat itu versi *stable* yang baru (14.2) masih dalam proses pengembangan. *Upgrade* ini menggunakan slackpkg. Dan tentu saja membutuhkan sambungan internet.

1.  Pilih cermin atau *mirror*. Dengan menyunting /etc/slackpkg/mirrors, menghilangkan tanda komentar/tanda pagar pada repo yang diinginkan. Tersedia banyak repo yang bisa dijadikan rujukan, tetapi sayangnya baru 2 repo lokal yang resmi terdaftar, yaitu *UI* dan *UKDW*. Saya gunakan milik UKDW karena lebih dekat (UKDW di Yogyakarta sedangkan saya di Semarang) sehingga harapannya lebih cepat. Bisa juga memilih repo *Slackware.com* yang secara otomatis akan memilihkan repo terdekat. Pastikan hanya 1 repo yang dipilih.
2.  *Update* daftar paket dengan melakukan slackpkg update
3.  *Upgrade* slackpkg untuk mendapatkan alamat repo 14.2. *Upgrade* juga glibc-solibs. Keduanya dapat dilakukan secara simultan : slackpkg upgrade slackpkg glibc-solibs
4.  Kalau muncul pertanyaan tentang konfigurasi baru, pilih saja O alias overwrite. Kalau tidak muncul lakukan slackpkg new-config
5.  Setelah *upgrade* slackpkg pilih repo lagi karena ada perubahan alamat/URL repo kemudian *update* lagi.
6.  Lanjut install paket-paket baru yang sebelumnya tidak ada : slackpkg install-new
7.  *Upgrade* sistem : slackpkg upgrade-all. Akan ditampilkan paket yang bisa di-*upgrade*. Hilangkan tanda bintangnya dengan menekan tombol spasi bila tidak ingin paket tersebut di-*upgrade* kemudian OK.
8.  Hapus paket yang tidak berguna. Paket yang perlu dihapus dan berbagai perubahan dari Slackware 14.1 ke 14.2 bisa dilihat [di sini](http://repo.ukdw.ac.id/slackware/slackware64-14.2/CHANGES_AND_HINTS.TXT) : slackpkg remove
9.  Karena ada pergantian kernel, jangan lupa konfigurasi ulang *boot loader* itu lilo atau elilo. Kalau menggunakan lilo : liloconfig. Kalau menggunakan elilo : eliloconfig
