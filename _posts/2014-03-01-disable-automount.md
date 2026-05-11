Walaupun diturunkan dari [debian](https://www.debian.org), **BlankOn Suroboyo** berbeda dengan debian karena pada Suroboyo secara default akan secara otomatis membuka media simpan (*flashdisk* misalnya) setelah media disambungkan ke komputer/laptop. Fitur ini dinamakan *automount-open media* yang agak mirip dengan *autorun* pada *windows*. Beberapa orang mungkin merasa terganggu dan ingin mematikan. Atau sebaliknya, pengguna debian justru ingin mengaktifkan fitur ini. Bagaimana cara mengaturnya?

```shell
gsettings set org.gnome.desktop.media-handling automount false
gsettings set org.gnome.desktop.media-handling automount-open false
```

Atau untuk tampilan grafisnya gunakan **dconf-editor / penyunting dconf** yang mana harus install dulu, sedangkan debian tidak usah karena **dconf-editor** sudah terpasang.

```shell
sudo apt-get  install dconf-editor
```

Kemudian jalankan **dconf-editor** melalui menu *Aplikasi \> Rupa-rupa \> Penyunting dconf*. Pilih

```shell
org.gnome.desktop.media-handling
```
Opsi **Automount** memberikan pilihan apakah akan mengaitkan/*mount* media secara otomatis. Jika diaktifkan (diberi tanda centang), maka *Nautilus* akan mengait otomatis media seperti *flashdisk* begitu ditancapkan. Sedangkan *Automount-open* memberikan pilihan apakah akan mengaitkan sekaligus membuka media begitu ditancapkan. 

