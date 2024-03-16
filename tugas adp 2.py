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
jarak= int(input("masukkan jarak ke rumah anda (dalam satuan meter) : "))

A1= A+D
A2= A+E 
A3= A+F 
B1= B+D 
B2= B+E 
B3= B+F 
C1= C+D 
C2= C+E 
C3= C+F
if menu == A :
    if jarak < 500 and jarak >= 0:
        print("tarif pesanan anda : " + "RP" + str(A1))
    elif jarak >= 500 and jarak <= 1500:
        print("tarif pesanan anda : " + "RP" + str(B1))
    else:
        print("tarif pesanan anda : " + "RP" + str(C1))
    
    

elif menu == B:
   if jarak < 500 and jarak >= 0:
       print("tarif pesanan anda : " + "RP" + str(A2))
   elif jarak >= 500 and jarak <= 1500:
       print("tarif pesanan anda : " + "RP" + str(B2))
   else:
       print("tarif pesanan anda : " + "RP" + str(C2))
   
 


elif menu == C :
   if jarak < 500 and jarak >= 0:
       print("tarif pesanan anda : " + "RP" + str(A3))
   elif  jarak >= 500 and jarak <= 1500:
       print("tarif pesanan anda : " + "RP" + str(B3))
   else:
       print("tarif pesanan anda : " + "RP" + str(C3))
   
   
else:
    print("menu yang anda masukkan tidak valid, mohon ulangi pesanan anda lagi")
    menu= input("pilih paket yang ingin anda pesan : ").upper()
    jarak= int(input("masukkan jarak ke rumah anda (dalam satuan meter) : "))
    if jarak < 500 and jarak >= 0 :
       if jarak < 500 and jarak >= 0:
          print("tarif pesanan anda : " + "RP" + str(A1))
       elif jarak >= 500 and jarak <= 1500:
          print("tarif pesanan anda : " + "RP" + str(B1))
       else:
          print("tarif pesanan anda : " + "RP" + str(C1))

    elif menu == B :
       if jarak < 500 and jarak >= 0:
          print("tarif pesanan anda : " + "RP" + str(A2))
       elif jarak >= 500 and jarak <= 1500:
          print("tarif pesanan anda : " + "RP" + str(B2))
       else:
          print("tarif pesanan anda : " + "RP" + str(C2))
    
    
    else :
       if jarak < 500 and jarak >= 0:
          print("tarif pesanan anda : " + "RP" + str(A3))
       elif jarak >= 500 and jarak <= 1500:
          print("tarif pesanan anda : " + "RP" + str(B3))
       else:
          print("tarif pesanan anda : " + "RP" + str(C3))

    

    


