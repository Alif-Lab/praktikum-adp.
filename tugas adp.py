print("program menentukan perbandingan luas sebuah segitiga dengan luas sebuah persegi panjang")

w = int(input("masukkan tinggi segitiga :"))
x = int(input("masukkan alas segitiga :"))
y = int(input("masukkan panjang persegi panjang :"))
z = int(input("masukkan lebar persegi panjang :"))

a = w*x/2
b = y*z
c = a/b

print("apakah luas segitiga sama dengan luas persegi panjang ?")
print(a==b)
print("perbandingan luas segitiga terhadap persegi panjang tersebut adalah : " + str(c))
