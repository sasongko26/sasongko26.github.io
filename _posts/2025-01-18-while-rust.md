---
date: 2025-01-18
title: While di rust
categories: [pemrograman]
tags: [rust]
---
_Looping_ memiliki peran penting dalam program. _Looping_ digunakan untuk menjalankan ulang blok kode ada menghentikannya. Jika kondisi terpenuhi maka _loop_ akan berjalan. Salah satu _loop_ yang disediakan **rust** adalah _while_.

Syntaxnya
```rust
while kondisi {
      ......
}
```
bagian bertitik-titik adalah blok kode yang akan dijalankan selama kondisinya terpenuhi.

Contoh: kita akan membuat _countdown_ yang sangat-sangat sederhana, yaitu menampilkan angka dari 10 sampai 1.

```rust
fn main(){
    let mut angka:u32 = 10;
    while angka >= 1 {
        println!("{angka}");
        angka -= 1;
    }
}
```
Mari kita bahas.

```rust
fn main(){
   ........
}
```
ini adalah fungsi utama **rust**. Semua program yang ditulis dengan **rust** tanpa fungsi main ini adalah _nonsense_! Ok, lanjut ke bagian bertitik-titik dalam blok fungsi main.

```rust
let mut angka:u32 = 10;
```
Kita mendefinisikan dengan _keyword_ let. Nama variabelnya adalah angka. Variabel ini bersifat _mutable_ karena didahului dengan mut. Bertipe data u32 yang merupakan bilangan bulat. 10 adalah nilai variabelnya.

```rust
while angka >=1 {
      .....
}
```
Syarat atau kondisinya adalah nilai variabel angka lebih dari atau sama dengan 1. Jika kondisi ini bernilai true atau terpenuhi, maka jalankan yang ada di titik-titik di dalam blok kode while.

```rust
println!("{angka}");
```
menampilkan nilai variabel angka.

```rust
angka -= 1;
```
Nilai variabel angka akan berubah, menjadi berkurang 1 dari sebelumnya.

Selesai. Insyaallah lanjut _looping_ lainnya.