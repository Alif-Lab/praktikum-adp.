def data(n):
    for i in range (n):
        x = int(input("masukkan angka :"))
        data1.append(x)
    return x
n=int(input("masukkan panjang array : "))

def mean(m):
    a=0
    for i in range (m):
        a += data1[i]
    b = a/m
    return b

def modus(data):

    data2= {}
    
    for i in data:
      if i in data2:
          data2[i] += 1
      else:
          data2[i] = 1

    max_data2=max(data2.values())

    data_modus=[i for i, f in data2.items() if f == max_data2]
    return data_modus

def variance(m):
    a=0
    rata2 = mean(m)
    for i in range (m):
        b=data1[i] 
        a= (b - rata2)**2
    d=a/(m-1)
    return d    



data1=[]
data(n)
m=len(data1)
mean(m)
modus(data1)
m=len(data1)
variance(m)

def hasil():
    rata2 = mean(m)
    Modus = str(modus(data1))
    variasi = variance(m)

    print ("|{:<9}|{:>6}|".format(("mean"),(rata2)))
    print ("|{:<9}|{:>6}|".format(("modus"),(Modus)))
    print ("|{:<9}|{:>6}|".format(("variance"),(variasi)))

hasil()