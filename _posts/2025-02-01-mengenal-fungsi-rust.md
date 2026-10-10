---
date: 2025-02-01
title: Mengenal fungsi di rust
categories: [pemrograman]
tags: [rust]
---
Kata fungsi yang dimaksud di catatan ini bukan kata yang bersinonim dengan kegunaan, melainkan istilah di bahasa pemrograman. Fungsi adalah sekumpulan baris kode yang biasanya dideklarasikan secara khusus untuk memudahkan dalam pemanggilan yang biasanya bisa berulang kali atau muncul di mana-mana. Karena di sini baru belajar, maka fungsinya yang sederhana saja.

Setiap catatan belajar **rust**, kami sertakan kode. Kode yang selalu ada dan harus ada ketika menulis program dengan **rust** adalah seperti ini

```rust
fn main(){

}
```
Ya, itulah fungsi main. Fungsi atau kode utama. Tanpa ini mustahil dikompilasi.

`fn` adalah keyword untuk mendeklarasikan fungsi.

`main` nama fungsinya. Penamaan ini sangat disarankan menggunakan _snake case_, yaitu apabila nama fungsinya lebih dari 1 kata maka ada tanda _underscore_  (\_) yang menghubungkan antarkata.

Yang berada di dalam kurung `()` adalah parameter. Sedangkan barisan kode yang akan dijalankan ditulis di bawahnya di antara kurung kurawal `{}`.

Bolehkah ada fungsi selain main? Semakin kompleks program semakin panjang kode. Di antara barisan kode tersebut mungkin ada yang bisa diringkas karena muncul beberapa kali. Seberapa banyak atau panjang kode yang ada di dalam gungsi? Tiada aturan baku. Sesuai kebutuhan saja. Kalau programnya sangat-sangat simpel tidak perlu membuat fungsi baru. Cukup masukkan ke fungsi main saja. Jika kompleks bisa dipertimbangkan membuat fungsi baru dan memanggil fungsi tersebut di dalam main.

Baiklah mari lanjutkan membuat contoh fungsi.

```rust
fn main(){
   tanya_kabar();
}

fn tanya_kabar(){
   println!("Halo, apa kabar?");
}

```

Kode di atas, di dalam fungsi main ada fungsi tanya_kabar yang akan menampilkan _Halo, apa kabar?_ . Nah, demikianlah tentang fungsi yang sangat sederhana. Selanjutnya, insyaallah di catatan berikutnya akan dilanjutnya dengan menuliskan parameter fungsinya.