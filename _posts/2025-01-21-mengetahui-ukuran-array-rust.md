date: 2025-01-21
title: Mengetahui ukuran array di rust
categories: [pemrograman]
tags: [rust]
---
Ukuran array yang dimaksud di sini adalah banyaknya elemen dari array. Sering juga disebut sebagai panjang array. Untuk mengetahuinya bisa memakai _method_ `len()`.

```rust
fn main(){
   let nilai = [80,90,100,95,80,70];
   println! ("Array nilai mempunyai {} elemen", nilai.len());
}
```