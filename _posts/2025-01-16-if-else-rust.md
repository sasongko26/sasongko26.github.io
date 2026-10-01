---
date: 2025-01-16
title: Menggunakan if else rust
categories: [pemrograman]
tags: [rust]
---
'if else' merupakan _keyword_ pada bahasa pemrograman **rust** yang digunakan untuk melakukan seleksi berdasarkan kondisi/syarat tertentu.

_Syntax_-nya adalah

```rust
if kondisi {
	statement untuk kondisi bernilai true;
}	else {
	statement untuk kondisi bernilai false;
}
```

Contoh kasus adalah untuk membedakan apakah seseorang termasuk orang kaya berdasarkan pengeluaran perbulannya. Misalnya, ditetapkan kriteria termasuk sebagai orang kaya jika pengeluarannya lebih dari atau sama dengan Rp10.000.000/bulan. Selain jumlah tersebut disebut bukan orang kaya.

Seseorang memiliki pengeluaran Rp8.000.000/bulan. Apakah dia orang kaya? Berikut kodenya
 
```rust
fn main(){
	let pengeluaran = 8000000;
	if pengeluaran >= 10000000 {
		println!("Pengeluaran {pengeluaran} termasuk orang kaya");
	} else {
		println!("Pengeluaran {pengeluaran} termasuk bukan orang kaya");
	}
}
```

Jika syarat atau kriterianya banyak, bisa menggunakan if else if. Contoh kasus adalah kategorisasi predikat berdasarkan Indeks Prestasi Kumulatif (IPK). Misalnya, predikatnya sebagai berikut:

| Rentang IPK | Predikat |
| 4.00 | Summa Cumlaude |
| 3.75 - 3.99 | Magna Cumlaude |
| 3.50 - 3.74 | Cumlaude |
| 2.75 - 3.49 | Sangat Memuaskan |
| 2.00 - 2.74 | Memuaskan |
| 0.01 - 1.99 | Gagal |

Kodenya

```rust
fn main(){
	let ipk:f32 = 3.72;
	if ipk == 4.00 {
		println!("IPK {ipk}. Predikat: Summa Cumlaude.");
	} else if ipk >= 3.75 && ipk < 4.00 {
		println!("IPK {ipk}. Predikat: Magna Cumlaude.");
	} else if ipk >= 3.50 && ipk < 3.75 {
		println!("IPK {ipk}. Predikat: Cumlaude.");
	} else if ipk >= 2.75 && ipk < 3.5 {
		println!("IPK {ipk}. Predikat: Sangat Memuaskan.");
	} else if ipk >= 2.00 && ipk < 2.75 {
		println!("IPK {ipk}. Predikat: Memuaskan.");
	} else if ipk >= 0.00 && ipk < 2.00 {
		println!("IPK {ipk}. Predikat: Gagal.");
	} else {
		println!("IPK {ipk} tidak valid.");
	}
}
```   
