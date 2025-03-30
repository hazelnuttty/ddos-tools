import requests
import os
import time

# Warna ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Token Default
TOKEN_DEFAULT = "Gv8@zP#1r$Xq5wL!"

# File untuk menyimpan data server
SERVER_FILE = "servers.txt"

# Cek token
def check_token():
    os.system("clear")
    print(f"""
{YELLOW}╔════════════════════════════════╗
║        🔑 LOGIN TOKEN 🔑        ║
╠════════════════════════════════╣
║ Masukkan token untuk mengakses ║
║ tools ini. Pastikan token benar║
╚════════════════════════════════╝{RESET}
""")
    token = input(f"{YELLOW}🔹 Masukkan Token: {RESET}")
    print(f"{YELLOW}Memverifikasi token...{RESET}", end="\r")
    time.sleep(1)

    if token != TOKEN_DEFAULT:
        print(f"{RED}❌ Token Salah! Keluar...{RESET}")
        time.sleep(2)
        exit()

# Cek apakah server Flask aktif
def check_server(server_url):
    try:
        response = requests.get(server_url + "/health", timeout=3)
        if response.status_code == 200:
            print(f"{GREEN}✅ Server aktif di {server_url}!{RESET}")
        else:
            print(f"{RED}❌ Server tidak merespons!{RESET}")
            exit()
    except requests.exceptions.ConnectionError:
        print(f"{RED}❌ Server tidak ditemukan! Jalankan server dulu.{RESET}")
        exit()

# Fungsi untuk menghentikan serangan
def stop_attack(server_url):
    try:
        response = requests.post(server_url + "/stop", timeout=5)
        if response.status_code == 200:
            print(f"{GREEN}✅ Serangan dihentikan!{RESET}")
        else:
            print(f"{RED}❌ Gagal menghentikan serangan!{RESET}")
    except requests.exceptions.RequestException:
        print(f"{RED}❌ Gagal menghubungi server!{RESET}")

# Fungsi untuk menambahkan server
def add_server():
    os.system("clear")
    print(f"""
{YELLOW}╔════════════════════════════════╗
║        ➕ ADD SERVER ➕        ║
╠════════════════════════════════╣
║ add server untuk disimpan      ║
╚════════════════════════════════╝{RESET}
""")
    server_url = input(f"{YELLOW}🔹 Masukkan URL server: {RESET}")
    if not server_url.startswith("http"):
        print(f"{RED}❌ URL tidak valid!{RESET}")
        time.sleep(2)
        return

    # Simpan URL server ke file
    with open(SERVER_FILE, "a") as file:
        file.write(server_url + "\n")
    print(f"{GREEN}✅ Server disimpan!{RESET}")
    time.sleep(2)

# Fungsi untuk menampilkan server yang disimpan
def show_servers():
    os.system("clear")
    print(f"""
{YELLOW}╔════════════════════════════════╗
║        📂 DAFTAR SERVER 📂          ║
╠════════════════════════════════╣
""")
    if os.path.exists(SERVER_FILE):
        with open(SERVER_FILE, "r") as file:
            servers = file.readlines()
            if servers:
                for index, server in enumerate(servers, 1):
                    print(f"{YELLOW}{index}. {server.strip()}{RESET}")
            else:
                print(f"{RED}❌ Tidak ada server yang disimpan.{RESET}")
    else:
        print(f"{RED}❌ File daftar server tidak ditemukan.{RESET}")
    print(f"{YELLOW}\nTekan Enter untuk kembali...{RESET}")
    input()

# Menu utama
def menu():
    os.system("clear")
    print(f"""
{YELLOW}╔════════════════════════════════════╗
║         🔥 PENTEST TOOL 🔥         ║
╠════════════════════════════════════╣
║ {GREEN}1.{RESET} 🎯 Masukkan Target               {YELLOW}║
║ {GREEN}2.{RESET} ⚔️ Jumlah Serangan             {YELLOW}  ║
║ {GREEN}3.{RESET} ⏳ Masukkan Delay             {YELLOW}  ║
║ {GREEN}4.{RESET} 🚀 Mulai Serangan                {YELLOW}║
║ {GREEN}5.{RESET} 🛑 Stop Serangan                 {YELLOW}║
║ {GREEN}6.{RESET} 📊 Monitor Server              {YELLOW}  ║
║ {GREEN}7.{RESET} ➕ Tambah Server               {YELLOW} ║
║ {GREEN}8.{RESET} 📂 Lihat Daftar Server        {YELLOW}   ║
║ {GREEN}9.{RESET} ❌ Keluar                     {YELLOW}  ║
╠════════════════════════════════════╣
║  Made by HAZELNUTT ❤            ║
╚════════════════════════════════════╝{RESET}
""")
    return input(f"{YELLOW}Pilih menu:{RESET} ")

# Variabel global
target_url = ""
attack_count = 0
delay = 0

check_token()

# Jalankan menu
while True:
    pilihan = menu()

    if pilihan == "1":
        target_url = input(f"{YELLOW}🔹 Masukkan URL target: {RESET}")
        if not target_url.startswith("http"):
            print(f"{RED}❌ URL tidak valid!{RESET}")
            time.sleep(2)
        else:
            print(f"{GREEN}✅ Target disimpan!{RESET}")
            time.sleep(1)

    elif pilihan == "2":
        try:
            attack_count = int(input(f"{YELLOW}🔹 Masukkan jumlah serangan: {RESET}"))
            if attack_count <= 0:
                raise ValueError
            print(f"{GREEN}✅ Jumlah serangan disimpan!{RESET}")
        except ValueError:
            print(f"{RED}❌ Masukkan angka yang valid!{RESET}")
        time.sleep(1)

    elif pilihan == "3":
        try:
            delay = float(input(f"{YELLOW}🔹 Masukkan delay antar request (detik): {RESET}"))
            if delay < 0:
                raise ValueError
            print(f"{GREEN}✅ Delay disimpan!{RESET}")
        except ValueError:
            print(f"{RED}❌ Masukkan angka delay yang valid!{RESET}")
        time.sleep(1)

    elif pilihan == "4":
        if not target_url or attack_count == 0:
            print(f"{RED}❌ Masukkan target & jumlah serangan dulu!{RESET}")
            time.sleep(2)
            continue

        print(f"\n{RED}🔥🔥 Mengirim permintaan ke server... 🔥🔥{RESET}")
        try:
            response = requests.post(target_url + "/start", json={
                "target": target_url,
                "count": attack_count,
                "delay": delay
            }, timeout=5)

            if response.status_code == 200:
                print(f"{GREEN}✅ Serangan dimulai di server!{RESET}")
            else:
                print(f"{RED}❌ Gagal memulai serangan!{RESET}")
        except requests.exceptions.RequestException:
            print(f"{RED}❌ Gagal menghubungi server!{RESET}")

        time.sleep(3)

    elif pilihan == "5":
        stop_attack(target_url)
        time.sleep(2)

    elif pilihan == "6":
        print(f"{YELLOW}📊 Monitoring server aktif di {target_url}...{RESET}")
        time.sleep(2)

    elif pilihan == "7":
        add_server()

    elif pilihan == "8":
        show_servers()

    elif pilihan == "9":
        print(f"{GREEN}✅ Keluar...{RESET}")
        time.sleep(2)
        exit()

    else:
        print(f"{RED}❌ Pilihan tidak valid!{RESET}")
