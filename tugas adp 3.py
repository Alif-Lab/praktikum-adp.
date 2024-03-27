p = 80
for i in range (1,p+1):
    if i% 4 == 0:
        x= "DOR"
    else:
        x= i
    print (x,end="  ")
    if i % 8 == 0:
        print()
    