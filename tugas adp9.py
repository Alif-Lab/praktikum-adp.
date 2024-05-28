from termcolor import colored, cprint
import os
import time

os.system('cls')

x= " "*3

for i in range (4):
    cprint(x,"red", "on_red",end="  ")
    
for i in range (8):
    cprint(" ","red", "on_red",end="")

print()

for i in range (5):
    if i < 3 :
        cprint(x,"red", "on_red",end=" ")
        print(end=" ")
        cprint(x,"red", "on_red",end=" ")
        print(end=" ")
        cprint(x,"red", "on_red",end=" ")
        print(end=" ")
        if i > 0 :
            cprint(x,"red", "on_dark_grey",end=" ")
        print(end=" ")
        if i > 0 :
            cprint(x,"red", "on_red",end=" ")
        print()
        
        
    else :
        cprint(x,"red", "on_red",end=" ")
        print(end=" ")
        print(" "*3,end=" ")
        print(end=" ")
        cprint(x,"red", "on_red",end=" ")
        print(end=" ")
        cprint(x,"red","on_dark_grey",end=" ")
        print(end=" ")
        cprint(x,"red", "on_red",end=" ")
        print()
        
    

    

    
    
    
    
        


