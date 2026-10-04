---
date: 2025-01-18
title: Loop break rust
categories: [pemrograman]
tags: [rust]
---
Melanjutkan catatan tentang **rust**. _Looping_ di **rust** juga bisa menggunakan **loop**. Penggunaannya untuk mengulang tanpa syarat. Tidak ada kondisi yang membatasi untuk terjadinya perulangan. Selama _statement_ itu berada di dalam blok **loop** maka ia akan terus dieksekusi.

```rust
loop {
     statement;
}
```

Contoh: akan menampilkan angka secara berurutan perbarisnya.

```rust
fn main(){
   let mut a:u32 = 1;
   loop {
        println!("{a}");
        a += 1;
   }
}
```
Ini secara _default_ tidak bisa dihentikan. Harus dihentikan paksa, misalnya dengan Ctrl C ataupun _close_ terminalnya.

Secara _coding_ **loop** bisa dihentikan dengan **break** pada saat mencapai kondisi tertentu. Misalnya **loop** di atas akan berhenti saat a bernilai 10. Maka kita tambahkan baris kondisi dan break di dalam blok **loop**.

```rust
loop {
     println!("{a}");
     a += 1;
     if a == 10 {
        break;
        }       
}
```

Nilai a terakhir yang ditampilkan adalah 9. Mengapa? Karena alur programnya adalah _assignment_ atau pemberian nilai ke a, tampilkan nilai a, tambahkan 1 ke nilai a berikutnya, begitu seterusnya sampai kondisi a bernilai 10 terpenuhi. Saat a bernilai 10, berarti sampai di tahapan _assignment_, kemudian break. Berhenti di sini. Belum sampai di `println!("{a}")`.

Selesai.