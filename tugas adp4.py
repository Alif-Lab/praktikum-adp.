print("daftar barang          harga     kode barang  ")
print("==============================================")
print("soda kaleng            Rp7.000        A")
print("teh botol              Rp5.000        B")
print("air mineral            Rp4.000        C")
print("roti coklat            Rp3.000        D")
print("roti keju              Rp3.000        E")
print("susu botol             Rp5.000        F")
print("mi rebus               Rp3.500        G")
print("mi goreng              Rp3.500        H")
print("saus sambal            Rp8.000        I")
print("saus tomat             Rp7.500        J")

print("PROMO BULAN INI")
print("~~soda kaleng diskon 10% setiap 5 atau lebih pembelian barang~~")
print("~~gratis 1 mi rebus setiap 8 pembelian~~")
print("~~setiap pembelian jenis mi apapun dalam kemasan dus harga = Rp120.000~~")
print("(satu dus berisi 40 pcs. untuk pembelian satu dus ketik 40 atau kelipatannya)")
print("~~saus sambal diskon 12.5% setiap 4 pembelian atau lebih~~")
print("~~setiap belanja lebih dari Rp150.000 diskon 10%~~")
total_harga= 0.0

while True:
    P= input("masukkan kode barang pesanan anda(tekan N jika selesai) :").upper()
    if P == "N" :
        break
    
    elif P == "A" :
        jumlah = int(input(f"jumlah {P} :"))
        x=7000*jumlah
        if jumlah >= 5:
            x= x*90/100
        else:
            x=x
        total_harga += x
        
    elif P == "B" :
        jumlah = int(input(f"jumlah {P} :"))
        x=5000*jumlah
        total_harga += x

    elif P == "C" :
        jumlah = int(input(f"jumlah {P} :"))
        x=4000*jumlah
        total_harga += x

    elif P == "D" :
        jumlah = int(input(f"jumlah {P} :"))
        x=3000*jumlah
        total_harga += x

    elif P == "E" :
        jumlah = int(input(f"jumlah {P} :"))
        x=3000*jumlah
        total_harga += x

    elif P == "F" :
        jumlah = int(input(f"jumlah {P} :"))
        x=5000*jumlah
        total_harga += x

    elif P == "G" :
        jumlah = int(input(f"jumlah {P} :"))
        x=3500*jumlah
        if jumlah>= 8:
            q=jumlah//8
            x=3500*(jumlah-q)
        elif jumlah % 40 == 0:
            y=jumlah/40
            x=120000*y
        else:
            x=x
        total_harga += x
     
    elif P == "H" :
        jumlah = int(input(f"jumlah {P} :"))
        x=3500*jumlah
        if jumlah% 40 == 0:
            y=jumlah/40
            x=120000*y
        else:
            x=x
        total_harga += x

    elif P == "I" :
        jumlah = int(input(f"jumlah {P} :"))
        x=8000*jumlah
        if jumlah >= 4:
            x=x*87.5/100
        else:
            x=x
        total_harga += x

    elif P == "J" :
        jumlah = int(input(f"jumlah {P} :"))
        x=7500*jumlah
        total_harga += x

    else :
        print("kode yang anda masukkan salah")

if total_harga >= 150000:
    total_harga = total_harga*90/100
else :
    total_harga = total_harga      
print(f"total harga pesanan anda  : Rp{total_harga}")