---
date: 2015-06-14
title: Jalankan sudo tanpa password
categories: [keamanan]
tags: [login, sudo]
---
Idealnya perintah sudo memang memerlukan password/kata sandi karena hakikat sudo itu pengguna “meminjam” hak *super user / root*. Tapi, password itu bisa saja kita hilangkan. Maksudnya, tidak perlu menuliskan password, contoh

```shell
wvdial 3
bash: wvdial: command not found
```

Baris 2, *command not found* menunjukkan 2 kemungkinan. Kemungkinan pertama, perintah yang diketikkan memang tidak ada. Kemungkinan kedua, perintah itu memerlukan hak *root*. Nah perintah [wvdial]({% post_url 2015-04-01-install-wvdial-slackware %}) ini yang bisa menjalankan adalah *root* atau *sudoers* (pengguna yang bisa menjalankan perintah hak *root* tapi dengan syarat memasukkan passwordnya root.

Wvdial ini kan perintah untuk konek internet via modem, rasanya tidak akan berbahaya kalau tidak dipassword. Caranya, edit /etc/sudoers. Untuk mengeditnya butuh hak root atau sudoers. Tambahkan baris dengan format berikut ke file tersebut.

```
pengguna hostname = NOPASSWD: perintah
```

- pengguna : nama pengguna yang termasuk dalam sudoers
- hostname : nama host
- perintah : ya perintah yang aslinya butuh password saat melakukan sudo yang ingin kita tidak pakai passwordnya

Contoh

```
sasongko laptopku = NOPASSWD: /usr/bin/wvdial
```

Nah, untuk selanjutnya, kalau login sebagai sasongko yang termasuk sudoers menjalankan perintah

```
sudo wvdial 
```

maka sasongko tidak akan diminta password dulu langsung jalan aja si wvdial
