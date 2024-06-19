from termcolor import colored, cprint
import os
import random



respon = {
    "hello": ["Hello!mau belanja apa hari ini?", "Hi! selamat datang di layanan online toko a", "hari yang cerah silahkan berbelanja"],
    "goodbye": ["terimakasih.", "See you later! Have a great day.", "Bye! Come back soon."],
    "menu": ["berikut menu yang akan ditampilkan","ini beberapa menu yang bisa anda pilih"],
    "feedback":["ada keluhan apa nih, silahkan komen untuk memberikan saran","maaf atas pelayanan kami jika anda kurang puas, saran anda sangat berarti untuk kami"],
    "default": ["keyword anda salah, ulangi lagi", "ulangi keyword yang sesuai dengan menu"]
}
def process_input(user_input):
    user_input = user_input.lower()
    for key in respon.keys():
        if key in user_input:
            return random.choice(respon[key])
    return random.choice(respon["default"])

def kasir(hari,nama,penjualan):
    with open("kasir.txt", "a") as file:
        file.write(f"hari : {hari}\n")
        file.write(f"kode barang: {nama}\n")
        file.write(f"banyak penjualan hari ini: {penjualan}\n")
    
def hari():
    hari = input("masukkan hari anda berbelanja : ")
    while True:
        if hari == "senin" or "selasa" or "rabu" or "kamis" or "jumat" or "sabtu" or "mingggu":
            break
        else:
            hari = input("masukkan hari anda berbelanja : ")
    return (hari)

def tampilkan():
    with open("kasir.txt", "r") as file:
        data = file.readlines()

    print("Data kasir:")
    for data in data:
        print(data.strip())

def tampilkan_feedback():
    with open("feedback.txt", "r") as file:
        data = file.readlines()

    print("feedback dari pelanggan:")
    for data in data:
        print(data.strip())

def belanja(x):
    total_belanja = 0
    while True:
        a = input("silahkan pilih belanjaan anda (ketik t untuk mengakhiri belanja): ")
        if a != "t":
            if a in menu:
                b =int( input("silahkan masukkan jumlah : "))
                c=int(a)
                if b <= banyak[c]: 
                   total_belanja += (menu[a]*b)
                   banyak[c] -= b
                   kasir(x,a,b)   
                else:
                    print("jumlah yang anda minta melebihi sisa yang tersedia")
                    print("silahkan pilih barang lain atau kurangi jumlah belanja anda")
            
            else :
                print("maaf,barang yang anda masukkan tidak tersedia")
        else:
            break
        
    print("total belanjaan anda senilai Rp.",end="") 
    cprint(total_belanja,"red")
    cprint("Chatbot: " + process_input("goodbye"),"white","on_green")

def feedback(email,pesan):
    with open("feedback.txt", "a") as file:
        file.write(f"alamat email pengguna: {email}\n")
        file.write(f"pesan atau saran pengguna: {pesan}\n")
    print("terimakasih atas saran yang telah anda berikan")
    print("balasan atas komplain yang anda ajukan akan dikirimkan secepatnya ke alamat email anda")

id = [
    "001",
    "002"
]
os.system('cls')

while True:
    menu = {
          "0" : 2000,
          "1" : 4000,
          "2" : 5000
           }
    nama = [
       ["roti","cola","ice cream"],
       [0,1,2]
           ]
 
    banyak = [100,100,50]

    
    fitur = input("pilih fitur yang akan diakses (k/b/quit): ").lower()

    if fitur == "k":
        data=input("masukkan id karyawan anda : ")
        if data in id:
           print("ketik ",end="")
           cprint("1 ","blue",end="")
           print("untuk ",end="")
           cprint("melihat penjualan","blue")

           print("ketik ",end="")
           cprint("2 ","blue",end="")
           print("untuk  ",end="")
           cprint("melihat feedback pembeli","blue")

           fitur_k = input(" masukkan 1/2 : ")

           if fitur_k == "1":
               tampilkan()

           elif fitur_k == "2":
               tampilkan_feedback()

           else :
               print("keyword salah") 
           
    elif fitur == "b":
        print("ketik ",end="")
        cprint("1 ","blue",end="")
        print("untuk mengakses fitur ",end="")
        cprint("belanja","blue")

        print("ketik ",end="")
        cprint("2 ","blue",end="")
        print("untuk mengakses fitur ",end="")
        cprint("feedback","blue")

        fitur_b = input("ketik 1/2 : ")

        if fitur_b == "1":
            print("Chatbot: " + process_input("hello"))
            print("Chatbot: " + process_input("menu"))
            x = len(nama)
            for i in range (x+1):
                print(f"{nama[0][i]} memiliki kode {nama[1][i]}")
            x = hari()
            belanja(x)

        elif fitur_b == "2":
            print("Chatbot: " + process_input("feedback"))
            email = input("masukkan alamat email anda : ")
            pesan = input("ketikkan saran, pesan atau pun komplain terhadap pelayanan ini: ")
            feedback(email,pesan)

        else:
            print("anda memasukkan keyword yang salah")

    elif fitur == "quit":
        cprint("terimakaih sudah menggunakan layanan ini untuk berbelanja","green")

        break

    else:
        print("anda memasukkan keyword yang salah")