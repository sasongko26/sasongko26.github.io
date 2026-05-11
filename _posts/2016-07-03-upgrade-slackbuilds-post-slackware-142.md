---
date: 2016-07-03
title: Upgrade slackbuild post slackware-14.2
categories: [manajemen paket]
---
Setelah melakukan [*upgrade* sistem ke *Slackware 14.2*]({% post_url 2016-07-03-upgrade-slackware-142 %}) ada baiknya *upgrade* juga paket yang diinstal dari slackbuilds.org.

1.  *Upgrade* sbopkg : sbopkg -u
2.  Versi sbopkg terbaru adalah 0.38.0 sedangkan yang terinstall 0.37.1. Untuk mengunduh versi terbaru ketik D
3.  Hasil unduhan : /tmp/sbopkg-0.38.0-noarch-1_wsr.tgz
4.  Setelah diunduh, *upgrade* : upgradepkg /tmp/sbopkg-0.38.0-noarch-1_wsr.tgz
5.  Karena menghasilkan konfigurasi baru, lakukan slackpkg new-config dan pilih overwrite saja.
6.  Kemudian *update* ke repo 14.2 : sbopkg pilih Utilities lalu Repository. Kemudian pilih SBo (14.2)
7.  Muncul konfirmasi, apakah akan membuat baru, pilih C untuk Create.
8.  Kemudian Back ke awal sbopkg, pilih Sync untuk *update* repo.
9.  Setelah *sync*-nya selesai, pilih EXIT kembali ke awal sbopk
10. Kemudian pilih Updates untuk mengecek paket apa saja yang bisa di-*upgrade*.
11. EXIT keluar konfirmasi apakah paket-paket tersebut akan dimasukkan ke dalam queue untuk bisa diinstall kemudian.YES untuk memasukkannya.
12. Kembali di awal sbopkg. Pilih Queue
13. PIlih Process akan muncul daftar paket langkah no.11
14. Silahkan pilih paketnya kemudian OK Kemudian Install dan OK
15. Tunggu sampai selesai.
16. Keluar dialog apakah akan menghapus yang ada di queue. Pilih Clear untuk menghapus. Kemudian keluar info bahwa queue sudah dihapus, keudian OK
17. Kembali ke Queue Menu pilih Back
18. Kembali ke awal sbopkg, karena sudah selesai, silahkan Exit
