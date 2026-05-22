---
date: 2025-01-10
title: Konstanta rust
categories: [pemrograman]
tags: [rust]
---
Konstanta dalam bahasa **rust** seperti variabel yang kita bisa mendeklarasikannya. Konstanta bisa mempunyai lingkup global; lebih luas dari pada variabel. Deklarasi konstanta harus dengan manifes yang menyebutkan eksplisit tipe datanya. Nama konstanta ditulis huruf kapital. *Keyword*-nya **const** atau **static**.

```rust
const NEGARA: &str = "Indonesia";
fn main(){
    const TANGGAL: u8 = 17;
    static BULAN: &str = "Agustus";
    static TAHUN: u16 = 1945;
    println!("Negara {} merdeka pada {} {} {}", NEGARA, TANGGAL, BULAN, TAHUN);
}
```
