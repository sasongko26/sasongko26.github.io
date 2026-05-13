---
date: 2014-03-23
title: Menggunakan wget download manager
categories: [jaringan]
tags:[wget]
---
Wget adalah download manager di linux. Secara default wget sudah terpasang dan bisa langsung digunakan. Wget sangat cocok digunakan untuk koneksi yang putus-nyambung-putus-nyambung-putus-nyambung atau keterbatasan kuota karena memiliki fitur resume. Cara menggunakannya mudah.

```shell
wget [url]
```
untuk mem-pause download tekan Ctrl+C. Dan untuk melanjutkan kembali tambahkan opsi -c.

```shell
wget [url] -c
```

Untuk lebih lengkapnya tentang wget ada di manual wget.

```shell
wget -h 
GNU Wget 1.15, adalah sebuah non-interaktif network retriever. 
Penggunaan: wget [PILIHAN]... [URL]... 

Argumen yang wajib untuk pilihan panjang juga wajib untuk pilihan yang pendek. 

Memulai: 
  -V,  --version           menampilkan versi dari Wget dan keluar. 
  -h,  --help              menampilkan bantuan ini. 
  -b,  --background        pergi ke background setelah memulai. 
  -e,  --execute=COMMAND   menjalankan sebuah perintah `.wgetrc'-style. 

Mencatat dan memasukan berkas: 
  -o,  --output-file=FILE     pesan log pada FILE. 
  -a,  --append-output=FILE  tambahkan pesan pada FILE. 
  -d,  --debug               tampilkan banyak informasi debugging. 
  -q,  --quiet               diam (tidak ada output). 
  -v,  --verbose             jadi verbose (ini yang default). 
   -nv, --no-verbose          matikan verboseness, tanpa menjadi quiet. 
       --report-speed=TYPE   Output bandwidth as TYPE.  TYPE can be bits. 
  -i,  --input-file=BERKAS    download URLs ditemukan dalam lokal atau BERKAS eksternal. 
  -F,  --force-html          perlakukan input file sebagai HTML. 
  -B,  --base=URL            telusuri berkas masukan HTML (-i -F) 
                             relatif ke URL. 
       --config=FILE         Specify config file to use. 

Download: 
  -t,  --tries=NUMBER            set nomor mencoba ke NUMBER (0 untuk tidak terbatas). 
       --retry-connrefused       coba lagi walaupun koneksi ditolak. 
  -O,  --output-document=FILE    tulis document pada FILE. 
  -nc, --no-clobber              skip downloads that would download to 
                                 existing files (overwriting them). 
  -c,  --continue                lanjutkan mengambil file yang terdownload  sebagian. 
       --progress=TYPE           pilih tipe gauge progress. 
  -N,  --timestamping            jangan mengambil kembali file kecuali file 
                                 lebih baru dari file local. 
  --no-use-server-timestamps     don't set the local file's timestamp by 
                                 the one on the server. 
  -S,  --server-response         tampilkan balasan server. 
       --spider                  jangan mendownload apapun. 
  -T,  --timeout=SECONDS         set semua nilai timeout pada SECONDS. 
       --dns-timeout=SECS        set the DNS lookup timeout pada SECS. 
       --connect-timeout=SECS    set the connect timeout pada SECS. 
       --read-timeout=SECS       set the read timeout pada SECS. 
  -w,  --wait=SECONDS            tunggu SECONDS diantara pengambilan. 
       --waitretry=SECONDS       tunggu 1..SECONDS diantara pencobaan dari sebuah pengambilan. 
       --random-wait             wait from 0.5*WAIT...1.5*WAIT secs between retrievals. 
       --no-proxy                secara eksplisit mematikan proxy. 
  -Q,  --quota=NUMBER            set pengambilan quota pada NUMBER. 
       --bind-address=ADDRESS    bind ke ADDRESS (hostname atau IP) pada local host. 
       --limit-rate=RATE         batasi kecepatan download ke RATE. 
       --no-dns-cache            matikan caching dari DNS lookups. 
       --restrict-file-names=OS  restrict karakter dalam nama file ke salah satu dari yang dibolehkan oleh OS. 
       --ignore-case             abaikan besar/kecil huruf ketika mencocokan files/direktori.. 
  -4,  --inet4-only              hanya menghubungi ke alamat IPv4 saja. 
  -6,  --inet6-only              hanya menghubungi ke alamat IPv6 saja. 
       --prefer-family=FAMILY    hubungi terlebih dahulu alamat dari family  yang dispesifikasikan, 
                                 salah satu dari IPv6, IPv4 atau none. 
       --user=USER               set kedua ftp dan http user pada USER. 
       --password=PASS           set kedua ftp dan http password pada PASS. 
       --ask-password            tanya untuk kata sandi. 
       --no-iri                  non-aktifkan dukungan IRI. 
       --local-encoding=ENC      gunakan ENC sebagai pengkodean lokal untuk IRI. 
       --remote-encoding=ENC     gunakan ENC sebagai pengkodean baku remote. 
       --unlink                  remove file before clobber. 

Direktori: 
  -nd,  --no-directories          jangan membuat direktori. 
  -x,  --force-directories        paksa pembuatan direktori. 
  -nH, --no-host-directories      jangan buat host directories. 
       --protocol-directories     gunakan nama protocol dalam direktori. 
  -P,  --directory-prefix=PREFIX  simpan file pada PREFIX/... 
       --cut-dirs=NUMBER           abaikan NUMBER remote komponen direktori. 

Pilihan HTTP: 
       --http-user=USER        set http user pada USER. 
       --http-password=PASS    set http password pada PASS. 
       --nocache               dissallow server-cached data. 
       --default-page=NAMA     Ubah nama halaman baku (biasanya 
                               ini `index.html'.). 
  -E,  --adjust-extension      simpan HTML/CSS dokumen dengan ekstensi yang sesuai. 
       --ignore-length         abaikan `Content-Length' bagian header. 
       --header=STRING         masukkan STRING dalam headers. 
       --max-redirect          batas maksimal yang diperbolehkan untuk redirection setiap halaman. 
       --proxy-user=USER       set USER sebagai username proxy. 
       --proxy-password=PASS   set PASS sebagai password proxy. 
       --referer=URL           masukkan `Referer: URL' header dalam HTTP request. 
       --save-headers          simpan HTTP headers pada file. 
  -U,  --user-agent=AGENT      identifikasi sebagai AGEN daripada sebagai Wget/VERSION. 
       --no-http-keep-alive    disable HTTP keep-alive (persistent koneksi). 
       --no-cookies            jangan menggunakan cookies. 
       --load-cookies=FILE     load cookies dari FILE sebelum session. 
       --save-cookies=FILE     simpan cookies pada FILE sesudah session. 
       --keep-session-cookies  load dan simpan session (non-permanen) cookies. 
       --post-data=STRING      gunakan metoda POST; kirim STRING sebagai data. 
       --post-file=FILE        gunakan metoda POST; kirim isi dari FILE. 
       --method=HTTPMethod     use method "HTTPMethod" in the header. 
       --body-data=STRING      Send STRING as data. --method MUST be set. 
       --body-file=FILE        Send contents of FILE. --method MUST be set. 
       --content-disposition   Lihat header Content-Disposition ketika memilih 
                               berkas lokal (EKSPERIMEN). 
       --content-on-error      output the received content on server errors. 
       --auth-no-challenge     Kirim informasi otentifikasi standar HTTP tanpa 
                               harus menunggu untuk ditanyai oleh server. 

Pilihan HTTPS (SSL/TLS): 
       --secure-protocol=PR     choose secure protocol, one of auto, SSLv2, 
                                SSLv3, TLSv1 and PFS. 
       --https-only             only follow secure HTTPS links 
       --no-check-certificate   jangan memvalidasi server certificate. 
       --certificate=FILE       client certificate file. 
       --certificate-type=TYPE  tipe sertifikate client, PEM atau DER. 
       --private-key=FILE       private key file. 
       --private-key-type=TYPE  tipe private key, PEM atau DER. 
       --ca-certificate=FILE    file yang berisi CA's. 
       --ca-directory=DIR       direktori dimana hash list dari CA's disimpan 
       --random-file=FILE       file dengan data acak untuk seeding SSL PRNG. 
       --egd-file=FILE          penamaan file EGD socket dengan data random. 

Pilihan FTP: 
       --ftp-user=USER         set ftp user pada USER. 
       --ftp-password=PASS     set ftp password pada PASS. 
       --no-remove-listing     jangan hapus file `.listing'. 
       --no-glob               matikan FTP nama file globbing. 
       --no-passive-ftp        disable the "passive" mode trasfer. 
       --preserve-permissions  preserver remote file permissions. 
       --retr-symlinks         ketika berekursif, ambil linked-to files (bukan dir). 

WARC options: 
       --warc-file=FILENAME      save request/response data to a .warc.gz file. 
       --warc-header=STRING      insert STRING into the warcinfo record. 
       --warc-max-size=NUMBER    set maximum size of WARC files to NUMBER. 
       --warc-cdx                write CDX index files. 
       --warc-dedup=FILENAME     do not store records listed in this CDX file. 
       --no-warc-compression     do not compress WARC files with GZIP. 
       --no-warc-digests         do not calculate SHA1 digests. 
       --no-warc-keep-log        do not store the log file in a WARC record. 
       --warc-tempdir=DIRECTORY  location for temporary files created by the 
                                 WARC writer. 

Recursive download: 
  -r,  --recursive          spesifikasikan untuk mendownload rekursif. 
  -l,  --level=NUMBER      maksimum kedalaman rekursi (inf atau 0 untuk tak terhingga). 
       --delete-after       delete files locally sesudah mendownloadnya. 
  -k,  --convert-links      buat links dalam HTML yang didownload atau CSS yang 
                            menunjuk ke berkas lokal. 
  --backups=N   before writing file X, rotate up to N backup files. 
  -K,  --backup-converted   sebelum mengubah file X, backup sebagai X.orig. 
  -m,  --mirror             shortcut untuk -N -r -l inf --no-remove-listing. 
  -p,  --page-requisites    ambil semua gambar, dll. yang diperlukan untuk menampilkan file HTML. 
       --strict-comments    hidupkan strick (SGML) handling dari komentar HTML. 

Recursive diterima/ditolak: 
  -A,  --accept=LIST               list yang dipisahkan oleh koma yang berisiekstensi yang diterima. 
  -R,  --reject=LIST               list yang dipisahkan oleh koma yang berisiekstensi yang ditolak. 
       --accept-regex=REGEX        regex matching accepted URLs. 
       --reject-regex=REGEX        regex matching rejected URLs. 
       --regex-type=TYPE           regex type (posix). 
  -D,  --domains=LIST              list yang dipisahkan oleh koma yang berisidomains yang dibolehkan. 
       --exclude-domains=LIST      list yang dipisahkan oleh koma yang berisidomains yang direject/tolak. 
       --follow-ftp                ikuti link FTP dari dokumen HTML. 
       --follow-tags=LIST          list yang dipisahkan oleh koma yang berisitag HTML yang diikuti 
       --ignore-tags=LIST          list yang dipisahkan oleh koma yang berisitag HTML yang diabaikan. 
  -H,  --span-hosts                pergi ke host asing ketika recursive. 
  -L,  --relative                  hanya mengikuti links relative saja. 
  -I,  --include-directories=LIST  list dari direktori yang dibolehkan. 
  --trust-server-names             use the name specified by the redirection 
                                   url last component. 
  -X,  --exclude-directories=LIST   list dari direktori yang diabaikan. 
  -np, --no-parent                 jangan merambah direktori atasnya. 

Laporkan bug dan saran kepada <bug-wget@gnu.org>
```
