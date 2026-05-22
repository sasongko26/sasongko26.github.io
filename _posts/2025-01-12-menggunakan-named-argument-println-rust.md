---
date: 2025-01-12
title: Menggunakan named argument pada println
categories: [pemrograman]
tags: [rust]
---
Untuk menampilkan pesan ke *standard output* yang biasanya adalah terminal emulator seperti konsole, xterm, alacritty, xfce-terminal, dll; **rust** menggunakan **println!**.

```rust
let nama = "Rustacean";
println!("Hai {}, selamat pagi!", nama);
```

output tersebut juga bisa dengan cara menggunakan *named argument*. *Named argument* kita memanggil variabel dengan memasukkannya ke dalam kurung kurawal. Hal ini berbeda dengan contoh-contoh sebelumnya, yang mana kurung kurawalnya kosong kemudian variabelnya disebutkan di akhir. Contoh di atas kalau diubah memakai *named argument* menjadi

```rust
let nama = "Rustacean";
println!("Hai {nama}, selamat pagi!");
```
