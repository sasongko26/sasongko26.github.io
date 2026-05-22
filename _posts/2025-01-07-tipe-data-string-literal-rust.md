---
date: 2025-01-07
title: Tipe data string literal rust
categories: [pemrograman]
tags: [rust]
---
**Rust** mengenal tipe data *string literal* (&str) atau *string slice*. Tipe data ini mirip dengan *char*, tetapi lebih banyak karakter yang bisa disimpan tidak hanya 1. *Assignment* dengan mengapit nilai variabel dengan tanda kutip.

Contoh:

```rust
fn main(){
   let nama = "Sasongko";
   println!("Halo, {}", nama);
   println!("Selamat belajar rust. Tetap semangat!");
}
```
