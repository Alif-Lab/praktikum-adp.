print("        DAFTAR HARGA PAKET MAKANAN          ")
print("____________________________________________")
print("|paket               |harga                |")
print("|____________________|_____________________|")
print("|A                   |Rp25.000             |")
print("|B                   |Rp30.000             |")
print("|C                   |Rp45.000             |")
print("|____________________|_____________________|")

print("            JARAK RUMAH ANDA                ")
print("____________________________________________")
print("|jarak rumah         |ongkir               |")
print("|____________________|_____________________|")
print("|kurang dari 500m    |gratis               |")
print("|500m - 1.5km        |Rp10.000             |")
print("|lebih dari 1.5km    |Rp20.000             |")
print("|____________________|_____________________|")

A= 25000
B= 30000
C= 45000

D=0
E=10000
F=20000

menu= (input("pilih paket yang ingin anda pesan : ")).upper()
jumlah= int(input("masukkan jumlah pesanan anda : "))
jarak= int(input("masukkan jarak ke rumah anda (dalam satuan meter) : "))

A1= A*jumlah+D
A2= A*jumlah+E 
A3= A*jumlah+F 
B1= B*jumlah+D 
B2= B*jumlah+E 
B3= B*jumlah+F 
C1= C*jumlah+D 
C2= C*jumlah+E 
C3= C*jumlah+F

if jarak < 500  :
    if menu == "A":
        print("tarif pesanan anda : " + "RP" + str(A1))
    elif menu == "B":
        print("tarif pesanan anda : " + "RP" + str(B1))
    else:
        print("tarif pesanan anda : " + "RP" + str(C1))
    
    

elif jarak >= 500 and jarak <= 1500 :
   if menu == "A":
       print("tarif pesanan anda : " + "RP" + str(A2))
   elif  menu == "B":
       print("tarif pesanan anda : " + "RP" + str(B2))
   else:
       print("tarif pesanan anda : " + "RP" + str(C2))
   
 


else :
   if menu == "A":
       print("tarif pesanan anda : " + "RP" + str(A3))
   elif  menu == "B":
       print("tarif pesanan anda : " + "RP" + str(B3))
   else:
       print("tarif pesanan anda : " + "RP" + str(C3))
   

    

    


