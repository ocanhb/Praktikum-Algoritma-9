def write_file():
    input_nama = input("masukkan nama kamu: ")
    input_umur = input("masukkan umur kamu: ")
    input_alamat = input("masukkan alamat tinggal kamu: ")
    input_email = input("masukkan email kamu: ")
    input_dosen_wali = input("masukkan nama dosen wali kamu: ")
    
    file_write = open("Biodata.txt", "w")
    file_write.write("Nama: " + input_nama + "\nUmur: " + input_umur + "\nAlamat: " + input_alamat +
                      "\nEmail: " + input_email + "\nDosen Wali: " + input_dosen_wali)
    file_write.close()

def read_file():
    file_read = open("Biodata.txt", "r")
    text = file_read.read()
    print("Berikut ini data kamu:")
    print(text)
    file_read.close()

write_file()
print("\n")
read_file()
