---
date: 2024-01-20
title: Variabel rust
categories: [pemrograman]
tags: [rust]
---
**Rust** mempunyai cara tersendiri untuk mendeklarasikan variabel, yaitu dengan diawali `let`. Kemudian, nama variabel dituliskan dengan huruf kecil semua dengan separator pemisah antarkata adalah *underscore* (\_). Contoh nama, kota_kelahiran, hasil_kali, dll.

Misalkan data kota kelahiran, akan kita deklarasikan sebagai kota_kelahiran

```rust
fn main(){
    let kota_kelahiran = "Jayapura";
}
```

Untuk menampilkan variabel tersebut, misalkan dengan macro println!() maka harus dengan *formatted print* yang mengandung **string literal**. String literal yang dimaksud adalah "{}",

```rust
fn main(){
    let kota_kelahiran = "Jayapura";
    println!("Kota Kelahiran adalah {}", kota_kelahiran);
}
```

