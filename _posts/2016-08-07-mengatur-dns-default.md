---
date: 2016-08-07
title: Mengatur DNS default
categories: [jaringan]
tags: [dns]
---
Secara *default*, DNS atau *Domain Name Server* yang digunakan adalah DNS dari operator/penyedia layanan internet. Namun sayangnya, operator tertentu kurang baik dalam penapisan/pemblokiran situs-situs negatif sehingga kadang konten-konten pornografi, judi, dan konten lainnya yang tidak sesuai dengan norma kesusilaan dan budaya Indonesia dapat sampai ke hadapan kita. Oleh karena itulah perlu menggunakan DNS lain.

Penggantian DNS ini ada 2 cara, yaitu manual dan otomatis.

Cara manual dengan menyunting berkas /etc/resolv.conf. Mengganti *nameserver* yang ada dengan *nameserver* yang diinginkan. Salah satu penyedia DNS penapisan situs negatif adalah [Nawala](http://nawala.id). *Nameserver* nya adalah:

- 180.131.144.144
- 180.131.145.145

Kelemahan cara ini setelah dinyalakan kembali maka kembali menggunakan dari operator. Untuk membuatnya menetap kita jadikan sebagai DNS *default* yang secara otomatis akan digunakan setiap kali konek dengan cara memasukkan DNS tersebut ke berkas /etc/dhcpcd.conf

Tambahkan

```
static domain_name_servers=180.131.144.144 180.131.145.145
```

di bawah

```
# A list of options to request from the DHCP server.
```

Sebenarnya sih bisa ditambah di baris manapun yang masih kosong, tapi biar tetap rapi dan sesuai kategori yang sudah dikelompokkan *Slackware* ya taruh saja di situ….hehehe…..

Jangan lupa *save*.
