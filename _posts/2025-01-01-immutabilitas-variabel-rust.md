---
date: 2025-01-01
title: Immutabilitas variabel rust
categories: [pemrograman]
tags: [rust]
---
Tak terasa hampir tepat setahun tidak menulis catatan tentang **rust**. Mengawali tahun 2025 ini, mari kita lanjutkan. Semoga bisa istiqamah dan khatam menulis catatan **rust**-nya.

Salah satu konsep menarik dari **rust** adalah immutabilitas variabel. Variabel secara *default* bersifat *immutable* alias tidak bisa diganti nilainya; hanya bisa di-*assign* 1x. **Rust** membedakan antara deklarasi dan *assignment*. Deklarasi adalah pendefinisian nama variabel dan tipe datanya, sedangkan *assignment* adalah pemberian nilai ke variabel tersebut. Deklarasi dilakukan lebih dulu, baru kemudian *assignment*. Memang biasanya ketika melakukan deklarasi sekalian *assignment*, walaupun sebenarnya kedua hal ini bisa juga dilakukan secara terpisah.

Deklarasi memerlukan *keyword* yaitu let.

```rust
let a;
```
berarti mendeklarasikan suatu variabel yang bernama a.

*Assignment* tidak memerlukan *keyword*, tetapi variabelnya harus sudah dideklarasikan.

```rust
a = 5;
```
memberikan nilai 5 ke dalam variabel a.

```rust
let a = 5;
```
berarti melakukan deklarasi sekaligus *assignment*.

Variabel secara *default* bersifat *immutable*. Jika sudah dideklarasikan bernilai 5 maka nilai tersebut tidak bisa diubah. Mari kita praktikkan

```rust
fn main(){
    let a = 5;
    println!("Nilai a awal: {}", a);
    a = 10;
    println!("Nilai a yang baru: {}", a);
}
```

Kita *compile* ternyata *error*.

```shell
error[E0384]: cannot assign twice to immutable variable `a`
 --> 02immutabilitasvariabel.rs:4:5
  |
2 |     let a = 5;
  |         - first assignment to `a`
3 |     println!("Nilai a awal: {}", a);
4 |     a = 10;
  |     ^^^^^^ cannot assign twice to immutable variable
  |
help: consider making this binding mutable
  |
2 |     let mut a = 5;
  |         +++

error: aborting due to 1 previous error

For more information about this error, try `rustc --explain E0384`.
```

Mengapa *error*? Baris ke-2 mendeklarasikan variabel a dan *assign* nilainya dengan 5. Sampai tahap ini masih oke. Baris ke-4 melakukan *assignment* ke variabel a dengan nilai 10, yang artinya mengubah nilai variabel a dari 5 ke 10. Secara *default* variabel bersifat *immutable*. Di sinilah masalahnya.

Lantas bagaimana solusinya? Ada 2 cara. Cara pertama seperti yang ditunjukkan pada *error message* saat *compile*, yaitu dengan menambahkan *keyword* mut antara let dan nama variabelnya (a). Ini adalah cara yang disarankan.

```rust
let mut a = 5;
```

*Keyword* mut menjadikan variabel a *mutable* alias bisa diganti atau di-*assign* lagi.

Cara ke-2 dengan membuat variabel baru dengan nama yang sama.

```rust
let a = 5;
println!("Nilai a awal: {}", a);
let a = 10;
println!("Nilai a yang baru: {}", a);
```
