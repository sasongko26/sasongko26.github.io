---
date: 2016-07-05
title: Virtmanager unable to connect libvirt
categories: [virtualisasi]
tags: [virt manager]
---
Melanjutkan [catatan kemarin]({% post_url 2016-07-04-virtmanager-no-module-requests %}), ternyata Virtual Manager belum bisa berjalan dengan baik. Sudah ada kemajuan sih dibanding yang kemarin, sudah bisa terbuka *graphical front-end*-nya, tapi ternyata kemudian muncul kotak dialog Virtual Machine Manager Connection Failure dengan detail sebagai berikut

```bash
Unable to connect to libvirt.

internal error: Cannot find suitable emulator for x86_64

Libvirt URI is: qemu:///system

Traceback (most recent call last):
  File "/usr/share/virt-manager/virtManager/connection.py", line 979, in _open_thread
    self._populate_initial_state()
  File "/usr/share/virt-manager/virtManager/connection.py", line 941, in _populate_initial_state
    logging.debug("conn version=%s", self._backend.conn_version())
  File "/usr/share/virt-manager/virtinst/connection.py", line 316, in conn_version
    self._conn_version = self._libvirtconn.getVersion()
  File "/usr/lib64/python2.7/site-packages/libvirt.py", line 3984, in getVersion
    if ret == -1: raise libvirtError ('virConnectGetVersion() failed', conn=self)
libvirtError: internal error: Cannot find suitable emulator for x86_64
```

Cek qemu apakah masih terinstall atau tidak. Harusnya sih memang terinstall karena saya belum pernah menghapusnya.

```bash
ls /var/log/packages|grep qemu
qemu-2.6.0-x86_64-1_SBo
```

Disebutkan **Unable to connect to libvirt** dengan Libvirt URI is: `qemu:///system`, dan `internal error: Cannot find suitable emulator for x86_64`, padahal terinstall **qemu** ini kan aneh. Pasti ada masalah dengan **qemu**-nya.

```bash
qemu-system-x86_64
```
output
```bash
qemu-system-x86_64: error while loading shared libraries: libcacard.so.0: cannot open shared object file: No such file or directory
```

Nah, ada titik terang. Masalah dependensi. libcacard tidak ada, berarti harus diinstall. Tapi installnya dari mana?

Pertama, asumsikan libcacard ini paket resmi dari **Slackware**. Cek dengan slackpkg

```bash
slackpkg search libcacard
```
output
```bash
Looking for libcacard in package list. Please wait... DONE

No package name matches the pattern.
```

Karena tidak ada, cek sbopkg karena qemu installnya dari sbopkg

```bash 
sbopkg -g libcacard
```
output
```bash
Searching for libcacard
Found the following matches for libcacard:
libraries/libcacard
```
OK, ketemu. Ada sbopkg-nya, install!

```bash
sbopkg -i libcacard
```

install selesai. Konfirmasi **qemu** dengan **qemu-system-x86_64** apakah masih bermasalah. Ternyata ok. Lanjut buka virt-manager-nya. Ok. Done! Alhamdulillah…
