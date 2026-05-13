---
date: 2022-05-25
title: Mengetahui spek RAM
categories: [hardware]
tags: [ram]
---
Identifikasi RAM yang ada di komputer merupakan hal mutlak untuk penggantian, upgrade ataupun sekedar membersihkan RAM. Informasi awal tentang RAM bisa diperoleh tanpa membongkar komputer ataupun laptop. Hal ini sangat bermanfaat bagi pengguna yang tidak punya keterampilan bongkar pasang komputer. Apalagi kalau masih garansi, kalau dibongkar bukan teknisi *service center* resminya maka garansinya hangus.

Untuk mengetahui spek RAM mudah. Bagi **slackers** (pengguna **Slackware**) tidak perlu repot menginstall macam-macam. *Tool*-nya sudah tersedia.

```shell
bash-5.1# dmidecode -t memory
# dmidecode 3.3
Getting SMBIOS data from sysfs.
SMBIOS 3.2.0 present.

Handle 0x0023, DMI type 16, 23 bytes
Physical Memory Array
        Location: System Board Or Motherboard
        Use: System Memory
        Error Correction Type: None
        Maximum Capacity: 64 GB
        Error Information Handle: Not Provided
        Number Of Devices: 4

Handle 0x0025, DMI type 17, 84 bytes
Memory Device
        Array Handle: 0x0023
        Error Information Handle: Not Provided
        Total Width: 16 bits
        Data Width: 16 bits
        Size: 3 GB
        Form Factor: DIMM
        Set: None
        Locator: A1_DIMM0
        Bank Locator: A1_BANK0
        Type: LPDDR4
        Type Detail: Synchronous
        Speed: 2133 MT/s
        Manufacturer: ABCD
        Serial Number: 1234
        Asset Tag: 9876543210
        Part Number: 123456789012345678
        Rank: Unknown
        Configured Memory Speed: 2133 MT/s
        Minimum Voltage: 1.1 V
        Maximum Voltage: 1.5 V
        Configured Voltage: 1.1 V
        Memory Technology: DRAM
        Memory Operating Mode Capability: Volatile memory
        Firmware Version: Not Specified
        Module Manufacturer ID: Unknown
        Module Product ID: Unknown
        Memory Subsystem Controller Manufacturer ID: Unknown
        Memory Subsystem Controller Product ID: Unknown
        Non-Volatile Size: None
        Volatile Size: 3 GB
        Cache Size: None
        Logical Size: None

Handle 0x0027, DMI type 17, 84 bytes
Memory Device
        Array Handle: 0x0023
        Error Information Handle: Not Provided
        Total Width: 16 bits
        Data Width: 16 bits
        Size: 3 GB
        Form Factor: DIMM
        Set: None
        Locator: A1_DIMM1
        Bank Locator: A1_BANK1
        Type: LPDDR4
        Type Detail: Synchronous
        Speed: 2133 MT/s
        Manufacturer: ABCD
        Serial Number: 1234
        Asset Tag: 9876543210
        Part Number: 123456789012345678
        Rank: Unknown
        Configured Memory Speed: 2133 MT/s
        Minimum Voltage: 1.1 V
        Maximum Voltage: 1.5 V
        Configured Voltage: 1.1 V
        Memory Technology: DRAM
        Memory Operating Mode Capability: Volatile memory
        Firmware Version: Not Specified
        Module Manufacturer ID: Unknown
        Module Product ID: Unknown
        Memory Subsystem Controller Manufacturer ID: Unknown
        Memory Subsystem Controller Product ID: Unknown
        Non-Volatile Size: None
        Volatile Size: 3 GB
        Cache Size: None
        Logical Size: None

Handle 0x0029, DMI type 17, 84 bytes
Memory Device
        Array Handle: 0x0023
        Error Information Handle: Not Provided
        Total Width: 16 bits
        Data Width: 16 bits
        Size: 3 GB
        Form Factor: DIMM
        Set: None
        Locator: A1_DIMM2
        Bank Locator: A1_BANK2
        Type: LPDDR4
        Type Detail: Synchronous
        Speed: 2133 MT/s
        Manufacturer: ABCD
        Serial Number: 1234
        Asset Tag: 9876543210
        Part Number: 123456789012345678
        Rank: Unknown
        Configured Memory Speed: 2133 MT/s
        Minimum Voltage: 1.1 V
        Maximum Voltage: 1.5 V
        Configured Voltage: 1.1 V
        Memory Technology: DRAM
        Memory Operating Mode Capability: Volatile memory
        Firmware Version: Not Specified
        Module Manufacturer ID: Unknown
        Module Product ID: Unknown
        Memory Subsystem Controller Manufacturer ID: Unknown
        Memory Subsystem Controller Product ID: Unknown
        Non-Volatile Size: None
        Volatile Size: 3 GB
        Cache Size: None
        Logical Size: None

Handle 0x002B, DMI type 17, 84 bytes
Memory Device
        Array Handle: 0x0023
        Error Information Handle: Not Provided
        Total Width: 16 bits
        Data Width: 16 bits
        Size: 3 GB
        Form Factor: DIMM
        Set: None
        Locator: A1_DIMM3
        Bank Locator: A1_BANK3
        Type: LPDDR4
        Type Detail: Synchronous
        Speed: 2133 MT/s
        Manufacturer: ABCD
        Serial Number: 1234
        Asset Tag: 9876543210
        Part Number: 123456789012345678
        Rank: Unknown
        Configured Memory Speed: 2133 MT/s
        Minimum Voltage: 1.1 V
        Maximum Voltage: 1.5 V
        Configured Voltage: 1.1 V
        Memory Technology: DRAM
        Memory Operating Mode Capability: Volatile memory
        Firmware Version: Not Specified
        Module Manufacturer ID: Unknown
        Module Product ID: Unknown
        Memory Subsystem Controller Manufacturer ID: Unknown
        Memory Subsystem Controller Product ID: Unknown
        Non-Volatile Size: None
        Volatile Size: 3 GB
        Cache Size: None
        Logical Size: None
```
Dari hasil tersebut bisa diketahui beberapa hal penting antara lain :

1.  Fisik RAM di *motherboard* (Location: System Board Or Motherboard)
2.  Kapasitas RAM maksimal 64 GB (Maximum Capacity: 64 GB)
3.  Tipe LPDDR4 (Type: LPDDR4)
4.  Ada 4 slot RAM (Number Of Devices: 4). Masing-masing slot 3 GB

