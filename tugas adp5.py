x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
y = []
n= len (x)

for i in range (n) :
    if x[i] > 0:
        a=x[i]**2
        b=2*x[i]
        c= a+b
        y.append(c)

    elif x[i] < 0:
        a=1/x[i]
        y.append(a)

    else :
        y.append(10)
print("|x  | f(x) |")
for i in range (n):
    print(f"|{x[i]} | {y[i]}|")

