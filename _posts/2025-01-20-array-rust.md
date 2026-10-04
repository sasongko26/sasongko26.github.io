---
date: 2025-01-20
title: Deklarasi array rust
categories: [pemrograman]
tags: [rust]
---
**Array** adalah kumpulan elemen dengan tipe data yang sama dan ukuran tetap. Deklarasi array hampir sama seperti deklarasi variabel: bisa secara eksplisit maupun inferensi. Deklarasi array secara eksplisit yang menyebutkan tipe data maka harus menyebutkan ukuran atau banyak elemennya juga. Contoh:

```rust
let nilai: [u32; 6] = [80,100,70,85,90,100];
let buah: [&str; 5] = ["pisang", "mangga", "apel", "belimbing", "alpukat"];
println!("{nilai:?}");
println!("{buah:?}");
```
Deklarasi di atas secara eksplisit. Ada 2 array yaitu nilai dan buah. Nilai mempunyai tipe data u32 dengan banyaknya elemen 6; dan buah mempunyai tipe data str dengan 5 element. Kemudian kedua array tersebut ditampilkan.