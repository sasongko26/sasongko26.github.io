---
date: 2025-01-13
title: Operator perbandingan rust
categories: [pemrograman]
tags: [rust]
---
**Rust** mengenal beberapa operator perbandingan, yaitu sama dengan (==), tidak sama dengan (!=), lebih kecil dari (\<), lebih kecil atau sama dengan (\<=), lebih besar dari (\>), lebih besar atau sama dengan (\>=). Hasil dari perbandingan ini adalah *bool*.

Contoh:

```rust
fn main(){
    let a = 5;
    let b = 10;
    let c = a == b;
    let d = a != b;
    let e = a < b;
    let f = a <= b;
    let g = a > b;
    let h = a >= b;
    println!("a = b ? {c}");
    println!("a != b ? {d}");
    println!("a < b ? {e}");
    println!("a <= b ? {f}");
    println!("a > b ? {g}");
    println!("a >= b ? {h}");
}
```
