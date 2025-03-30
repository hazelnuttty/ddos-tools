---

## *Pentest Tool - README*

## Deskripsi

Pentest Tool adalah alat yang digunakan untuk melakukan serangan uji penetrasi (pentesting) pada server target. Dengan menggunakan alat ini, Anda dapat mengonfigurasi berbagai parameter serangan seperti URL target, jumlah serangan, dan delay antar permintaan. Alat ini juga memungkinkan Anda untuk menambah dan memonitor server yang diserang.

Fitur Utama

Login dengan Token: Untuk mengakses tool ini, pengguna harus memasukkan token yang valid.

Menambahkan Server: Menambahkan URL server yang ingin diserang.

Mengonfigurasi Serangan: Memasukkan target, jumlah serangan, dan delay antar request.

Memulai dan Menghentikan Serangan: Menjalankan dan menghentikan serangan pada server yang dipilih.

Monitoring Server: Memantau status server yang diserang.

Menyimpan Daftar Server: Menyimpan daftar server yang dapat digunakan kembali di masa depan.


Prasyarat

Python 3.x

Library requests


## Cara Instalasi

1. Clone Repository
```sh
git clone https://github.com/username/repository-name.git
cd repository-name
```

3. Instalasi Dependencies Pastikan Anda sudah memiliki Python 3 dan pip terinstall. Kemudian, instal library yang diperlukan:
```sh
pip install -r requirements.txt
```sh
Jika requirements.txt tidak ada, Anda bisa langsung menginstal library requests:
```sh
pip install requests
```

3. Jalankan Script Untuk menjalankan Pentest Tool, cukup jalankan skrip berikut:

python pentest_tool.py

## Server
Kami memakai sistem server indenpenden, pengguna harus mengistall di dua di device yang berbeda, Opsi kedua... jika pengguna tidak menginstall server pada dua hp maka hp yang menjadi sistem akan terbebani.
```sh
git clone
```

## Cara Penggunaan

1. Login dengan Token Setelah menjalankan aplikasi, Anda akan diminta untuk memasukkan token. Masukkan token yang benar untuk melanjutkan.


2. Menambah Server Pilih menu Tambahkan Server dan masukkan URL server yang ingin Anda tambahkan ke dalam daftar server.


3. Konfigurasi Serangan

Pilih menu Masukkan Target dan masukkan URL target yang ingin diserang.

Pilih menu Jumlah Serangan dan tentukan jumlah serangan yang diinginkan.

Pilih menu Delay dan tentukan delay antar permintaan.



4. Mulai dan Hentikan Serangan Setelah konfigurasi serangan selesai, pilih menu Mulai Serangan untuk memulai serangan ke server yang ditentukan. Anda dapat menghentikan serangan dengan memilih menu Stop Serangan.


5. Monitoring Server Pilih menu Monitor Server untuk memantau status server yang diserang.


6. Lihat Daftar Server Anda dapat melihat daftar server yang telah Anda simpan dengan memilih menu Lihat Daftar Server.



Struktur File
```sh
pentest_tool/
│
├── pentest_tool.py     # Skrip utama
├── servers.txt         # File untuk menyimpan daftar server
└── requirements.txt    # Daftar dependensi Python (opsional)
```
## License

MIT License

---

Jika ada tambahan atau perubahan, silakan beri tahu saya!
