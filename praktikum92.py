def create_file():
    filename = input("Masukkan nama file: ")
    with open(filename, 'w') as file:
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        angkatan = input("Masukkan angkatan: ")
        sahabat = input("Masukkan nama sahabat: ")
        catatan = input("Masukkan catatan: ")
        file.write(f"Nama: {nama}\nNIM: {nim}\nAngkatan: {angkatan}\nNama Sahabat: {sahabat}\nCatatan: {catatan}\n")
        print(f"File {filename} telah dibuat.")

def add_text_to_file():
    filename = input("Masukkan nama file yang ingin ditambahkan teks: ")
    sahabat_text = input("Masukkan nama sahabat: ")
    catatan_text = input("Masukkan catatan: ")
    with open(filename, 'a') as file:
        file.write(f"Nama Sahabat: {sahabat_text}\nCatatan: {catatan_text}\n")
        print(f"Teks berhasil ditambahkan ke dalam file {filename}.")

def read_file():
    filename = input("Masukkan nama file yang ingin dibaca: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Isi dari file {filename}:\n{content}")
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")

def main():
    while True:
        print("\nPilih menu:")
        print("1. Buat file")
        print("2. Baca file")
        print("3. Tambahkan teks ke file")
        print("4. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4): ")

        if choice == '1':
            create_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            add_text_to_file()
        elif choice == '4':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
