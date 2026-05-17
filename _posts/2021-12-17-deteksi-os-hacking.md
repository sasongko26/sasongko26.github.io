---
date: 2021-12-17
title: Deteksi sistem operasi target hacking
categories: [jaringan]
tags: [nmap]
---
Judul catatan kali ini sedikit berbeda dibanding sebelumnya. Ada **hacking**-nya. Hehehehe…. Tapi itu tidak menunjukkan bahwa kemampuan penulis dalam ilmu **hacking** bagus. Hanya bisa itu tok.

*Information gathering* merupakan tahap krusial dalam proses **hacking** maupun **cracking**. Salah satu kegiatan *information gathering* adalah *scanning* atau deteksi sistem operasi yang digunakan pada target. Deteksi ini perlu karena berbeda sistem operasi mungkin membutuhkan teknik yang berbeda.

Deteksi menggunakan **nmap** yang secara *default* sudah tertanam di **slackware**. Kasus kali ini alamat target adalah 192.168.106.250. Hasil *scanning* menunjukkan beberapa informasi, antara lain sistem operasi, port yang terbuka dan webserver yang digunakan.

```shell
nmap -A 192.168.106.250
Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-17 13:26 WIB
Nmap scan report for 192.168.106.250
Host is up (0.0071s latency).
Not shown: 985 closed tcp ports (reset)
PORT      STATE SERVICE     VERSION
21/tcp    open  ftp         Microsoft ftpd
| ftp-syst:
|_  SYST: Windows_NT
80/tcp    open  http        Apache httpd 2.4.12 ((Win32) OpenSSL/1.0.1l PHP/5.6.8)
|_http-server-header: Apache/2.4.12 (Win32) OpenSSL/1.0.1l PHP/5.6.8
| http-title: XAMPP 5.6.8
|_Requested resource was http://192.168.106.250/xampp/
135/tcp   open  msrpc       Microsoft Windows RPC
139/tcp   open  netbios-ssn Microsoft Windows netbios-ssn
443/tcp   open  ssl/http    Apache httpd 2.4.12 ((Win32) OpenSSL/1.0.1l PHP/5.6.8)
|_http-server-header: Apache/2.4.12 (Win32) OpenSSL/1.0.1l PHP/5.6.8
| http-title: XAMPP 5.6.8
|_Requested resource was https://192.168.106.250/xampp/
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
554/tcp   open  rtsp?
2869/tcp  open  http        Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
2968/tcp  open  enpp?
3389/tcp  open  tcpwrapped
|_ssl-date: 2021-12-17T06:30:56+00:00; +22s from scanner time.
| ssl-cert: Subject: commonName=Usr-PC
| Not valid before: 2021-10-20T00:50:03
|_Not valid after:  2022-04-21T00:50:03
| rdp-ntlm-info:
|   Target_Name: USR-PC
|   NetBIOS_Domain_Name: USR-PC
|   NetBIOS_Computer_Name: USR-PC
|   DNS_Domain_Name: Usr-PC
|   DNS_Computer_Name: Usr-PC
|   Product_Version: 6.1.7600
|_  System_Time: 2021-12-17T06:29:50+00:00
10243/tcp open  http        Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49152/tcp open  msrpc       Microsoft Windows RPC
49153/tcp open  msrpc       Microsoft Windows RPC
49154/tcp open  msrpc       Microsoft Windows RPC
49155/tcp open  msrpc       Microsoft Windows RPC
49156/tcp open  msrpc       Microsoft Windows RPC
MAC Address: 50:3E:AA:33:D2:BD (Tp-link Technologies)
Device type: general purpose
Running: Microsoft Windows 7|2008|8.1
OS CPE: cpe:/o:microsoft:windows_7::- cpe:/o:microsoft:windows_7::sp1 cpe:/o:microsoft:windows_server_2008::sp1 cpe:/o:microsoft:windows_server_2008:r2 cpe:/o:microsoft:windows_8 cpe:/o:microsoft:windows_8.1
OS details: Microsoft Windows 7 SP0 - SP1, Windows Server 2008 SP1, Windows Server 2008 R2, Windows 8, or Windows 8.1 Update 1
Network Distance: 1 hop
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 21s, deviation: 0s, median: 21s
|_smb2-security-mode: SMB: Couldn\'t find a NetBIOS name that works for the server. Sorry!
|_nbstat: NetBIOS name: nil, NetBIOS user: <unknown>, NetBIOS MAC: 50:3e:aa:33:d2:bd (Tp-link Technologies)
|_smb2-time: ERROR: Script execution failed (use -d to debug)

TRACEROUTE
HOP RTT     ADDRESS
1   7.10 ms 192.168.106.250

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 247.54 seconds
```
