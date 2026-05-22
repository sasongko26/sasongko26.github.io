---
date: 2021-01-15
title: Sintaks komentar rust
categories: [pemrograman]
tags: [rust]
---
Komentar pada **rust** yang biasa digunakan ada 2 jenis, yaitu komentar baris dan komentar blok. Komentar baris diberikan dengan sintaks `//` pada awal komentar. Semua yang ada setelah tanda `//` pada baris tersebut akan dianggap sebagai komentar yang tidak akan dieksekusi. Komentar blok untuk memberikan komentar pada blok kode atau beberapa baris kode. Semua baris yang ada di antara /\* dan \*/ dianggap sebagai komentar.

Contoh komentar baris

```rust
// ini adalah komentar yang tidak akan dieksekusi
fn main(){
    println!("Hai");
}
```

Contoh komentar blok

```rust
/* ini adalah komentar
yang tidak akan
dieksekusi
*/
```

