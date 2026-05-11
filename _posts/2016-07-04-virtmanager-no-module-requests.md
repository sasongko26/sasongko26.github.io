---
date: 2016-07-04
title: VirtManager no module request
categories: [virtualisasi]
tags: [virt manager]
---
Setelah [upgrade slackbuilds]({% post_url 2016-07-03-upgrade-slackbuilds-post-slackware-142 %}) kemarin ternyata **Virtual Machine Manager** tidak bisa dijalankan.

```bash
virt-manager
```
output
```bash
Traceback (most recent call last):
  File "/usr/share/virt-manager/virt-manager", line 33, in <module>
    from virtinst import util as util
  File "/usr/share/virt-manager/virtinst/__init__.py", line 89, in <module>
    from virtinst.distroinstaller import DistroInstaller
  File "/usr/share/virt-manager/virtinst/distroinstaller.py", line 23, in <module>
    from . import urlfetcher
  File "/usr/share/virt-manager/virtinst/urlfetcher.py", line 34, in <module>
    import requests
ImportError: No module named requests
```

Ternyata, ada masalah dependensi. `ImportError: No module named requests` menunjukkan tidak adanya _modul requests_, atau tidak terinstall paket **python-requests**. Ini dibuktikan dengan *output* `ls /var/log/packages|grep python-request` yang kosong.

Terus bagaimana?

Install python-requests melalui sbopkg

```bash
sbopkg -i python-requests
```
