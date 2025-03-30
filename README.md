## Pentest Tool

Pentest Tool adalah alat yang dirancang untuk melakukan uji penetrasi (pentesting) pada server target. Dengan menggunakan alat ini, pengguna dapat menyesuaikan berbagai parameter serangan, seperti URL target, jumlah serangan, dan interval delay antara setiap permintaan. Tool ini memungkinkan pengguna untuk menambah, mengonfigurasi, dan memonitor server yang sedang diserang, serta menyimpan daftar server yang dapat digunakan di masa depan.

Fitur Utama:

- Login dengan Token: Pengguna harus memasukkan token valid untuk mengakses alat ini.
- Menambahkan Server: Pengguna dapat menambahkan URL server target untuk diserang.
- Mengonfigurasi Serangan: Alat ini memungkinkan pengaturan URL target, jumlah serangan, dan delay antar permintaan.
- Memulai dan Menghentikan Serangan: Pengguna dapat menjalankan dan menghentikan serangan pada server yang dipilih.
- Monitoring Server: Memantau status server yang sedang diserang untuk melihat apakah server tersebut masih aktif atau   mengalami gangguan.
- Menyimpan Daftar Server: Menyimpan URL server yang telah diserang atau yang ingin diserang kembali di masa depan.

#  Cara Instalasi:

1. Clone Repository:
Clone repository dengan perintah:
```sh
git clone https://github.com/username/repository-name.git
cd repository-name
```

2. Instalasi Dependencies:
Pastikan Python 3 dan pip telah terinstall di perangkat Anda. Instal library yang diperlukan:
```sh
pip install -r requirements.txt
```sh
Jika tidak ada file requirements.txt, instal langsung library requests:
```sh
pip install requests
```

3. Jalankan Script:
Untuk menjalankan Pentest Tool, gunakan perintah: python pentest_tool.py

---

## Server
Kami telah menyediakan server langsung yang terhubung dengan ddos-tools, Kalian bisa coba menginstall nya.
```sh
git clone https://github.com/hazelnuttty/server-independen.git
```

---
## Cara Penggunaan

1. Login dengan Token:
Saat pertama kali menjalankan aplikasi, Anda akan diminta untuk memasukkan token yang valid. Masukkan token untuk melanjutkan ke fitur lainnya.

2. Menambah Server:
Pilih menu Tambahkan Server dan masukkan URL server yang ingin Anda serang.



3. Konfigurasi Serangan:
Masukkan target URL yang ingin diserang.
Tentukan jumlah serangan yang ingin dilakukan.
Atur interval delay antar setiap permintaan.

4. Mulai dan Hentikan Serangan:
Setelah konfigurasi serangan selesai, pilih Mulai Serangan untuk menjalankan serangan pada server yang telah dipilih. Gunakan menu Stop Serangan untuk menghentikan serangan.

5. Monitoring Server:
Gunakan menu Monitor Server untuk melihat status server yang sedang diserang.

6. Lihat Daftar Server:
Untuk melihat daftar server yang telah disimpan, pilih menu Lihat Daftar Server.

---
## Struktur File:
```sh
pentest_tool/
├── pentest_tool.py     # Skrip utama
├── servers.txt         # File untuk menyimpan daftar server
└── requirements.txt    # Daftar dependensi Python (opsional)
```
## License:

MIT License

Copyright (c) 2025 hazelnuttty

Izin diberikan, tanpa biaya, kepada siapa pun yang memperoleh salinan perangkat lunak ini dan dokumentasi terkait (perangkat lunak), untuk menggunakan perangkat lunak tanpa batasan, termasuk tanpa batasan hak untuk menggunakan, menyalin, memodifikasi, menggabungkan, menerbitkan, mendistribusikan, mensublisensikan, dan/atau menjual salinan perangkat lunak, serta untuk memungkinkan orang lain yang diberikan perangkat lunak untuk melakukan hal tersebut, dengan syarat-syarat berikut:

Pemberitahuan hak cipta di atas dan pemberitahuan izin ini harus disertakan dalam semua salinan atau bagian penting dari perangkat lunak ini.

PERANGKAT LUNAK INI DIBERIKAN "SEBAGAIMANA ADANYA", TANPA JAMINAN APAPUN, BAIK TERSURAT MAUPUN TERSIRAT, TERMASUK NAMUN TIDAK TERBATAS PADA JAMINAN TERHADAP KELAYAKAN UNTUK DIPERDAGANGKAN, KESESUAIAN UNTUK TUJUAN TERTENTU, ATAU PELANGGARAN HAK CIPTA. DALAM HAL APAPUN, PENGARANG ATAU PEMEGANG HAK CIPTA TIDAK BERTANGGUNG JAWAB ATAS KERUGIAN APAPUN, BAIK DALAM TINDAKAN KONTRAK, TORT, ATAU SEBALIKNYA, YANG TIMBUL DARI, DIKARENAKAN, ATAU BERKAITAN DENGAN PERANGKAT LUNAK INI ATAU PENGGUNAANNYA.

---
Jika Anda membutuhkan penambahan atau perubahan, jangan ragu untuk memberi tahu saya!

