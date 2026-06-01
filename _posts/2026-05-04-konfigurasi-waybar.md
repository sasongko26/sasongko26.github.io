---
date: 2026-05-04
title: Konfigurasi dasar waybar
categories: [desktop]
tags: [waybar]
---
**Waybar** adalah bar atau panel ringan yang dibuat untuk **wayland**. _Wayland compositor_ seperti **labwc, sway, hyprland** dll disarankan bisa menggunakannya. Adanya bar ini memudahkan untuk identifikasi dan/atau intervensi ke sistem. Fitur yang sangat kami butuhkan sehingga menggunakan **waybar** adalah indikator baterai. Pengguna laptop tentu sangat dimudahkan jika ada indikator baterai. Misalnya untuk memutuskan apakah perlu segera di-_charge_ atau sudah penuh. Fitur lain, antara lain indikator audio, jaringan, cpu, memori, suhu, capslock/numlock, baterai dan jam.

**Waybar** membawa pengaturan _default_ di `/etc/xdg/waybar`. Jika ingin melakukan perubahan sesuai kebutuhan atau selera tentu saja bisa. Tinggal ubah konfigurasinya. Perubahan konfigurasi ini kami lebih suka _per user_ bukan global agar ketika _upgrade_ dan ada perubahan konfigurasi _default_, kami tidak perlu mengubah lagi. Biasanya _upgrade_ akan menimpa file konfigurasi _default_.

Konfigurasi _user_ ada di `~/.config/waybar`. Jika direktori ini tidak ada atau kosong bisa _copas_ dari _default_.

```shell
cp -r /etc/xdg/waybar/ ~/.config/
```

Direktori konfigurasi tersebut berisi 2 file: `config.jsonc` untuk pengaturan _module_ atau _item_ apa saja yang ada di bar, dan `style.css` untuk mengatur bagaimana tampilannya. 