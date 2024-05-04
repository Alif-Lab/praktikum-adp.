m = int(input("masukkan ukuran baris matriks A : "))
n = int(input("masukkan ukuran kolom matriks A : "))
A = []
for i in range (n):
    barisA = []
    for j in range (m):
        x = int(input(f"baris {i+1} kolom {j+1} : "))
        barisA.append(x)
    A.append(barisA)


p = int(input("masukkan ukuran baris matriks B : "))
q = int(input("masukkan ukuran kolom matriks B : "))
B = []
for i in range (q):
    barisB = []
    for j in range (p):
        x = int(input(f"baris {i+1} kolom {j+1} : "))
        barisB.append(x)
    B.append(barisB)
print()
print("matriks A :", A)
print()
print("matriks B :", B)
print()
print("matriks C = A x B")

if n==p :
    C = []
    for i in range (q):
        barisC = []
        for j in range (m):
            x=0
            for k in range (n):
                y= A[k][j]*B[i][k]
                x += y
            barisC.append(x)
            x=x-x
        C.append(barisC)
    print("matriks C :", C)
    
   
else :
    invalid = "invalid matrix multiplication"
    print(invalid)

print()

print("matriks D = A transpose + B transpose")

AT = []

BT = []

for i in range (m):
    at = []
    for j in range (n):
       x=A[j][i]
       at.append(x)
    AT.append(at)

for i in range (p):
    bt = []
    for j in range (q):
       y=B[j][i]
       bt.append(y)
    BT.append(bt)

D = []
if m==p:
    if n==q:
        for i in range (m):
            barisD = []
            for j in range (n):
                z = AT[i][j]+BT[i][j]
                barisD.append(z)
            D.append(barisD)
        print("matriks D :", D)   

    else:
        print("invalid matrix summation") 

else:
    print("invalid matrix summation")




