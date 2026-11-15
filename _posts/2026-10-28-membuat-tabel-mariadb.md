---
date: 2026-10-28
title: Membuat tabel mariadb
categories: [database]
tags: [mariadb]
---
Tabel mempunyai peran penting dalam sistem database relasional. Tanpanya data tidak bisa disusun secara rapi. Catatan kali ini adalah tentang membuat tabel. Pembuatan tabel sebagai fondasi database tentu saja dengan **mariadb**. Alhamdulillah **mariadb** secara _default_ sudah _terinstall_ di **slackware**, jadi kami selaku _slackers_ langsung menggunakannya saja.

Langkah pertama, tentu saja [login mariadb]({% post_url 2026-10-18-login-mariadb %}) dengan _username_ dan _password_ yang sesuai. Kemudian kita masuk atau gunakan database di mana tabel tersebut menjadi komponennya. Sebagai contoh, di sini kami gunakan nama database adalah kampus.

```sql
USE nama_database;
```
ganti `nama_database` dengan yang sesuai, Jika sesuai contoh nama database yang kami gunakan, maka _command_-nya menjadi
```sql
USE kampus;
```
Langkah berikutnya, pastikan _field_ atau kolom apa yang membentuk tabel. Jenis dan jumlah _field_ ini disesuaikan dengan tabelnya. Misal, database kampus tentang kampus atau perguruan tinggi atau yang awamnya menjadi jawaban dari `kuliah di mana?`. Tabel apa yang ada di database kampus? Banyak! Salah satunya adalah tabel dosen. Coba diinventarisasi _field_ apa yang perlu dibuat. Paling tidak adalah

1. `id` atau nomor urut, bertipe integer atau bilangan bulat, dan nomor urut bertambah secara otomatis.
2. `nama_lengkap`, bertipe varchar dengan panjang karakter 100. Panjangnya bisa disesuaiakan, tapi kami harap 100 karakter sudah cukup dan bisa mengakomodir nama lengkap yang panjang, dan kolom ini tidak boleh kosong.
3. `gelar_depan`, bertipe varchar juga, tetapi panjangnya bisa lebih pendek dari `nama_lengkap` karena umumnya gelar yang ditulis di depan nama tidak banyak.
4. `gelar_belakang`, bertipe varchar juga, dengan panjang bisa panjang karena tidak menutup kemungkinan seseorang punya gelar yang sambung-menyambung menjadi satu... hehe....

_Field_ lain bisa ditambahkan sesuai kebutuhan.

Nah, selesai menyusun konsep _field_ mari tuliskan dalam _sql_

```sql
CREATE TABLE dosen (
       id INT PRIMARY KEY AUTO_INCREMENT,
       nama_lengkap VARCHAR(100) NOT NULL,
       gelar_depan VARCHAR(50),
       gelar_belakang VARCHAR(100)
);
```
Jika muncul `Query OK` berarti sukses! Selamat! Untuk rekonfirmasi atau memastikan tabel sudah dibuat, bisa dicek dengan [menge-_list_ tabel yang ada]({% post_url 2026-10-22-mengetahui-daftar-tabel-mariadb %}). Insyaallah berlanjut ke catatan berikutnya.