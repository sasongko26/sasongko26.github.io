---
date: 2025-01-11
title: Deklarasi banyak variabel rust
categories: [pemrograman]
tags: [rust]
---
**Rust** mengakomodir deklarasi beberapa variabel sekaligus dalam 1 *statement*. Caranya dengan memasukkan semua variabel ke dalam kurung dan antarvariabel diberi separator/pemisah tanda koma. Contoh:

Deklarasi variabel satu persatu

```rust
let negara = "Indonesia";
let tahun_merdeka: u16 = 1945;
```

Kedua *statement* tersebut bisa diringkas

```rust
let (negara, tahun_merdeka: u16) = ("Indonesia", 1945);
```
