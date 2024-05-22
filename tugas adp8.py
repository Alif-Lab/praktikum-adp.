film = {  
        
    
}
for key, value in film.items():
    print(f"{key:<14} : {value}")

def tambah_film(judul, penulis, sutradara, tahun):
    with open("film.txt", "a") as file:
        file.write(f"judul film : {judul}, penulis skenario : {penulis}, penulis skenario : {penulis}, tahun rilis : {tahun}\n")
    print("Data film berhasil ditambahkan.")

def hapus_judul(judul):
    with open("film.txt", "r") as file:
        lines = file.readlines()
    with open("film.txt", "w") as file:
        for line in lines:
            if line.split(",")[0] != judul:
                file.write(line)
    print("Data film berhasil dihapus.")

def edit_film(judul, penulis, sutradara, tahun):
    with open("film.txt", "r") as file:
        lines = file.readlines()
    with open("film.txt", "w") as file:
        for line in lines:
            if line.split(",")[0] == judul:
                file.write(f"judul film : {judul}, penulis skenario : {penulis}, penulis skenario : {penulis}, tahun rilis : {tahun}\n")
            else:
                file.write(line)
    print("Data film berhasil diubah.")

def tampilkan_semua_data_film():
    with open("film.txt", "r") as file:
        film = file.readlines()
    if film:
        print("Data film:")
        for data in film:
            print(data.strip())
    else:
        print("Database film kosong.")

while True :
    print("Menu:")
    print("1. Tambah film")
    print("2. Hapus film")
    print("3. Edit film")
    print("4. Tampilkan Semua data film")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
       judul = input("Masukkan judul: ")
       penulis = input("Masukkan nama penulis skenario: ")
       sutradara = input("Masukkan nama sutradara: ")
       tahun = input("Masukkan tahun rilis: ")
       tambah_film(judul, penulis, sutradara, tahun)
    elif pilihan == "2":
       judul = input("Masukkan judul film yang ingin dihapus : ")
       hapus_judul(judul)
    elif pilihan == "3":
       judul = input("Masukkan judul film yang ingin diubah : ")
       penulis = input("Masukkan nama penulis skenario : ")
       sutradara = input("Masukkan nama sutradara : ")
       tahun = input("Masukkan tahun rilis : ")
       edit_film(judul, penulis, sutradara, tahun)
    elif pilihan == "4":
       tampilkan_semua_data_film()
    elif pilihan == "5":
       print("Terima kasih telah menggunakan program ini.")
       break
    else:
       print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")