---
date: 2025-01-09
title: Deklarasi variabel rust
categories: [pemrograman]
tags: [rust]
---
**Rust** menyediakan 2 cara deklarasi variabel. Cara pertama dengan inferensi, yaitu dengan tidak menuliskan tipe datanya. Cara ini seperti yang selama ini sudah ada di contoh-contoh catatan kami tentang **rust**. **Rust** akan menebak dan mengatur secara otomatis. Jika tidak didefinisikan, bilangan bulat akan diberikan tipe i32, sedangkan bilangan rasional f64. Cara kedua dengan manifes yaitu menuliskan tipe datanya. Cara menuliskannya yaitu dengan memberikan tanda titik dua setelah nama variabel diikuti dengan tipe datanya.

Contoh dengan inferensi:

```rust
let nama = "Sasongko";
let jumlah_rumah = 2;
```

Pada contoh di atas kita tidak mendefinisikan tipe datanya apa. Sehingga **rust** akan memberikan tipe data secara default.

Contoh dengan manifes:

```rust
let nama: &str = "Sasongko";
let jumlah_rumah: u8 = 2;
```

</div>

Contoh kedua ini, variabel nama kita berikan tipe data string literal, dan variabel jumlah_rumah sebagai *unsigned integer* u8.
