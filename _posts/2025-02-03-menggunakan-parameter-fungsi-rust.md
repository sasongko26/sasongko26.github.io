---
date: 2025-02-03
title: Menggunakan parameter fungsi rust
categories: [pemrograman]
tags: [rust]
---
Melanjutkan tentang [fungsi]({% post_url 2025-02-01-mengenal-fungsi-rust %}). Fungsi yang dibahas sebelumnya adalah fungsi yang sangat sederhana, tidak menggunakan parameter karena apa yang diproses bersifat tetap/selalu sama. Bagaimana jika yang akan diproses itu membutuhkan perhitungan yang bisa berganti nilai masukannya? Contoh menghitung luas, menampilkan apa yang diinput pengguna, dll. Pada kasus seperti inilah perlu adanya parameter.

Parameter adalah variabel yang dimasukkan ke dalam fungsi. Adanya parameter membuat fungsi lebih fleksibel, tidak perlu menulis kode dengan logika sama berulang kali.

_Syntax_ umum fungsi dengan parameter
```rust
fn nama_fungsi(parameter1: tipe1, parameter2: tipe2) {
   // penggunaan parameter
}
```
Contoh:
```rust
fn salam{nama: &str}{
   println!("Selamat pagi, {nama}");
}

fn main(){
   salam("Indonesia");
}
```

Ada 2 fungsi: salam dan main. Fungsi salam mempunyai parameter nama bertipe _string_, Fungsi salam akan menampilkan tulisan "Selamat pagi." yang diikuti nama yang sudah dimasukkan. Kemudian fungsi salam ini dipanggil di fungsi utama/main agar bisa dikompilasi dan berjalan sebagaimana mestinya.