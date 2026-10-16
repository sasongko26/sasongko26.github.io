---
date: 2025-02-05
title: For in rust
categories: [pemrograman]
tags: [rust]
---
Pengulangan di bahasa pemrograman **rust** bisa menggunakan [loop]({% post_url 2025-01-18-loop-break-rust %}) atau [while]({% 2025-01-18-while-rust %}) atau `for in`. Catatan ini membahas yang ketiga.

`for in` biasanya digunakan untuk pengulangan sesuai dengan jumlah yang berada dalam rentang yang ditentukan. Contoh, akan menampilkan angka. Penampilan angka ini akan berulang sesuai rentang, katakanlah angka yang akan muncul adalah angka 1 sampai 5 yaitu 1, 2, 3 dan 4. `for in` rentangnya adalah **sampai** tidak **sampai dengan**. Berikut contoh kodenya

```rust
fn main(){
   for i in 1..5 {
   println!("{i}");
   }
}
```

Selesai.