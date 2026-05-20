---
date: 2016-12-12
title: Enable TLP on i3wm
categories: [hardware, manajemen daya]
tags: [tlp, battery]
---
Beberapa hari yang lalu install i3 (i3wm) menggunakan sbopkg. Biasanya, dengan *desktop environment* lain seperti *Mate*, baterai bisa bertahan 4 - 6 jam. Namun, dengan *i3* belum 3 jam sudah minta dicas, padahal penggunaannya seperti biasa tidak ada perbedaan signifikan.

Cek powertop ternyata banyak yang **Bad** seperti *default*-nya tanpa TLP. Padahal *service* TLP saat *booting* jalan, *Tunable* di powertop hanya 1 yang **Bad** lainnya **Good** semua.

I3 memiliki berkas konfigurasi /etc/i3/config. Konfigurasi itu yang saya gunakan. Berkas tersebut juga bisa diisi *script* atau aplikasi yang jalan saat i3 di-*start*. Di berkas ini saya masukkan *service* TLP untuk di-*restart* ketika masuk i3. Yang perlu diperhatikan, pengguna *login* sebagai *user* biasa bukan *root*, sedangkan untuk me-*restart* TLP butuh hak akses root.

Nah, di sinilah saya menggunakan sesuatu yang sebenarnya tidak terlalu saya sukai, yaitu sudo. Mengapa saya tidak terlalu menyukai sudo?. Karena **Slackware** sudah diketahui *password* rootnya yang dibuat saat install. Berbeda dengan *Ubuntu, Linux Mint* dan anak cucunya yang memang butuh sudo karena *password* rootnya secara *default* sangat misterius antah berantah.

```shell
echo "exec_always sudo /etc/rc.d/rc.tlp restart" >> /etc/i3/config
echo "sasongko ALL=(ALL) NOPASSWD: /etc/rc.d/rc.tlp restart" >> /etc/sudoers
# silahkan ganti 'sasongko' dengan user Anda
```

Untuk *booting* selanjutnya TLP akan tetap jalan walau di i3 sekalipun.
