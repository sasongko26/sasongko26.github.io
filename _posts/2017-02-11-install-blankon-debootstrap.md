---
date: 2017-02-11
title: Install blankon dengan debootstrap
categories: [manajemen paket]
tags: [debootstrap]
---
Hari ini, sabtu, 11 Januari 2017, hujan turun lagi. Dan di kala hujan deras dan *nggrejih* begini sejak pagi, *suwung* pun melanda. Tiba-tiba terbersit untuk *install* **BlankOn** yang telah lama saya tinggalkan.

Teringat, DVD/USB *installer*-nya sudah tak ada. Iso-nya pun terhapus. *So, what’s next*? Download iso **BlankOn**? Ide bagus, tapi sayang kuota tak mencukupi. Beli DVD/USB tak memungkinkan. Harus pesan dulu, sampai di tangan paling cepat besok senin, keburu sudah tidak *kepengin installl* lagi. Hahahaha….

Ya pakai debootstrap sajalah. Lagian belum pernah pakai debootstrap sebelumnya. debootstrap tersedia di SBo sehingga semakin memudahkan. Tapi biar lebih greget sekaligus hemat kuota *install*-nya varian yang minbase saja, paket super minimalis.

Terpikirkan 2 skenario *install*:

1.  *Install minbase* dari repo **Debian**, kemudian *upgrade* ke *tambora*.
2.  *Install minbase* dari repo **BlankOn**.

Sepertinya skenario nomor 1 sudah *mainstream*, jadi pakai nomor 2 biar greget. Skenario lengkapnya, varian yang diinstall minimal, arsitektur 64 bit (amd64), hanya komponen *main*, menggunakan *script* sendiri yang namanya *tambora*, diinstal ke partisi yang saya mount ke /media/hd1, ambil dari repo **BlankOn**.

Karena tidak ada *script* untuk **BlankOn** di debootstrap, bikin sendiri saja. **BlankOn** terbaru (**Tambora**) mengambil paket dari **Debian Sid**, maka untuk *script*-nya modifikasi saja dari *sid*. Copas dulu, beri nama *tambora*. Sebenarnya nama baru ini sih suka-suka, tapi biar lebih gampang dan sesuai tujuan, namai saja *tambora*.

```shell
cp /usr/share/debootstrap/scripts/sid /usr/share/debootstrap/scripts/tambora
```
Walaupun *Tambora* diturunkan dari *Sid*, tetap perlu penyesuaian *script*.

```shell
vim /usr/share/debootstrap/scripts/tambora
```

Baris 5 ganti debian menjadi blankon sehingga menjadi keyring /usr/share/keyrings/blankon-archive-keyring.gpg.

Next,

```shell
debootstrap --variant=minbase --arch=amd64 --components=main tambora /media/hd1 http://arsip.blankonlinux.or.id/blankon/
```
Setelah proses itu selesai, ternyata tidak ter-*install* kernel, entah mengapa terjadi belum mencari penyebabnya. Kalau **Tambora** ini mau dijalankan pakai chroot dari **Slackware** maka misi telah selesai! Tapi kalau *pengin* bisa dijalankan secara mandiri, brarti mau tidak mau ya harus *install kernal*. *Kernel* yang ada di repo masih jadul ik tapi, 3.10. Biar ajalah.

```shell
chroot /media/hd1
apt install linux-image-3.10-3-amd64
exit
```

Selesai? Belum. Skema partisi hardisk saya **GPT** yang menggunakan **EFI**. Kabarnya, agar bisa di-*install* dengan EFI harus pakai haftian. Ah, ini kan saya *install* bukan dari iso tapi debootstrap. Masih perlu pakai haftian? Dan *bootloader* yang saya gunakan *bootloader* bawaan **Slackware** yaitu elilo, sedangkan secara *default* **BlankOn** pakai grub. Jadi bagaimana?

Masukkan *kernel* dan *initrd*-nya ke partisi EFI.

```shell
cp /media/hd1/boot/vmlinuz-3.10-3-amd64 /boot/efi/EFI/Slackware/blankon
cp /media/hd1/boot/initrd.img-3.10-3-amd64 /boot/efi/EFI/Slackware/
```

dan jangan lupa edit elilo.conf-nya. tambahkan

```shell
image=blankon
  label=blankon
  initrd=initrd.img-3.10-3-amd64
  read-only
  append="root=/dev/sda8 vga=normal ro"
```

Partisi root yang saya gunakan untuk **BlankOn Tambora** adalah */dev/sda8*. Dan ketika di-*boot*, sukses! Alhamdulillah. 
