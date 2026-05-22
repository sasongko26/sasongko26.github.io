---
date: 2025-01-11
title: Operator aritmatika rust
categories: [pemrograman]
tags: [rust]
---
Operator aritmatika yang dimiliki **rust** adalah penjumlahan (+), pengurangan (-), perkalian (\*), pembagian, dan modulus atau sisa pembagian. Operasi aritmatika hanya bisa dijalankan terhadap variabel yang bertipe data sama.

```rust
const A: f32 = 10.0;
const B: f32 = 20.0;
fn main(){
    println!("A = {}", A);
    println!("B = {}", B);
    println!("A + B = {}", A+B);
    println!("A - B = {}", A-B);
    println!("A x B = {}", A*B);
    println!("A : B = {}", A/B);
    println!("A mod B = {}", A%B);
    println!("B mod A = {}", B%A);
}
```
