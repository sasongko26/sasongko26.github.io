---
date: 2023-01-12
title: Coding pertama rust
categories: [pemrograman]
tags: [rust]
---
**Rust** bahasa pemrograman yang saat ini sedang naik daun digadang-gadang sebagai suksesor C maupun C++. Rust sudah banyak digunakan bahkan rencananya masuk sebagai *second language* pada kernel linux sebagai pendamping C. Hal ini ditandai dengan adanya akomodasi **rust** mulai kernel 6.1.

File *source code* **rust** berekstensi .rs. **Rust** memerlukan kompilasi untuk dapat dijalankan karena **rust** adalah *compiled language*. Ada 2 cara kompilasi, yaitu dengan rustc/ apabila programnya simple hanya terdiri dari 1 file .rs dan tanpa adanya dependensi, atau dengan cargo kalau programnya kompleks.

Jamaknya belajar bahasa pemrograman dimulai dengan **hello world**. Berikut adalah *source code* dari **hello world**.

```rust
fn main(){
    println!("Hello, World!");
}
```

Setiap program **rust** mengharuskan adanya suatu fungsi. Fungsi utama **rust** bernama *main*. Fungsi didefinisikan dengan fn. Penulisan nama fungsi diikuti tanda kurung () dan kurung kurawal {}. *Statement* dalam fungsi diakhir dengan *semicolon* atau titik koma di ujung baris. Apabila di akhir baris tidak ada *semicolon*, maka baris tersebut akan dianggap sebagai satu kesatuan *statement* dengan baris di bawahnya.

println!() adalah *macro* untuk menampilkan *output* yang diikuti dengan baris baru/pergantian baris. Karena ingin menampilkan *output* Hello, World! maka ini dimasukkan ke dalam kurung.

Lalu bagaimana untuk eksekusi atau menjalankannya? *Source code* ini harus dikompilasi/*compile* menjadi *binary* dulu. *Binary* inilah yang akan dieksekusi. Untuk kompilasi, karena hanya 1 file .rs dan misalkan nama filenya adalah hello.rs, maka kompilasinya

```shell
rustc hello.rs
```

Kompilasi tersebut menghasilkan file *binary* hello. Bisa dieksekusi dengan

```shell
./hello
```
