def data(n):
    for i in range (n):
        x = int(input("masukkan angka :"))
        data1.append(x)
    return x

def mean(m):
    a=0
    for i in range (m):
        a += data1[i]
    b = a/m
    return b

def modus(x):
    array = [0] * (max(data1)+1)

    for i in x :
        array[i] += 1

    max_array = max(array)

    modus = []

    for i in x:
        if array[i] == max_array :
            if i  not in modus:
                modus.append(i)
    
    return modus

def variance(m):
    a=0
    rata2 = mean(m)
    for i in range (m):
        b=data1[i] 
        a= (b - rata2)**2
    d=a/(m-1)
    return d    

def hasil():
    rata2 = mean(m)
    Modus = str(modus(data1))
    variasi = variance(m)

    print ("|{:<9}|{:>6}|".format(("mean"),(rata2)))
    print ("|{:<9}|{:>6}|".format(("modus"),(Modus)))
    print ("|{:<9}|{:>6}|".format(("variance"),(variasi)))


n =int(input("masukkan panjang array : "))
data1=[]
data(n)
m=len(data1)
mean(m)
modus(data1)
m=len(data1)
variance(m)
hasil()