---
date: 2026-09-01
title: Menggunakan labwc
categories: [desktop]
tags: [labwc, wayland]
---
Kalau kita mencari _wayland compositor_ yang ringan dan bisa _stacking_ maka **labwc** adalah jawabannya. Apalagi **Slackware** menyediakannya sebagai paket resmi (saat catatan ini ditulis aada di  _current_) menunjukkan **labwc** bukanlah _project_ sembarangan. Instalasi mudah. Begitu juga penggunaannya.

Biasanya, _slackers_ menggunakan **labwc** untuk meningkatkan _user experience_ saat menjalankan _xfce on wayland_. Ya, dukungan wayland di xfce memang masih terbatas, tetapi arah ke sana sudah ada. 

Menjalankan **labwc** mudah. Jalankan

```shell
labwc
```

atau 

```shell
dbus-run-session labwc
```

# Konfigurasi

Konfigurasi berada di di ~/.config. Jika direktori ini kosong sangat mungkin **labwc** yang dijalankan hanya akan menampilkan _blackscreen_. Klak-klik _mouse_ sana-sini juga tidak menghasilkan apa-apa. Terdapat 2 file utama yang seharusnya ada di direktori ini: autostart dan rc.xml.

**labwc** akan menjalankan autostart segera setelah **labwc** start. Karena suka ada bar atau panel saya masukkan [waybar]({% post_url 2026-05-02-install-waybar %}) ke autostart. 

```shell
#!/bin/bash
waybar &
fuzzel --daemon & > /dev/null &
```
Untuk memudahkan menjalankan aplikasi saya juga memasukkan [fuzzel]({% post_url 2026-05-05-install-fuzzel %}) ke autostart.

Pengaturan berikutnya adalah tentang bagaimana membuat tombol pintasan keyboard. Pengaturan ini ada di rc.xml. Berikut contohnya

```xml
<?xml version="1.0"?>
<labwc_config>
  <keyboard>
    <keybind key="W-f">
      <action name="Execute">
	<command>fuzzel --log-level=error</command>
      </action>
    </keybind>

    <keybind key="W-Return">
      <action name="Execute">
	<command>foot</command>
      </action>
    </keybind>

	<keybind key="W-e">
      <action name="Execute">
        <command>emacs</command>
      </action>
    </keybind>
    
    <keybind key="A-Tab">
      <action name="NextWindow"/>
    </keybind>

    <keybind key="A-S-Tab">
      <action name="PreviousWindow"/>
    </keybind>

    <keybind key="W-L">
      <action name="Execute">
	<command>swaylock</command>
      </action>
    </keybind>
	

  </keyboard>
</labwc_config>
```
