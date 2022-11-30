i=1
j=4
while(i<10):
    for c in range(0,9):
        print(" ",end="")
    for a in range(j,0,-1):
        print(" ",end="")
    for b in range(0,i):
        print("*",end="")
    i=i+2
    j=j-1
    print()
i=9
j=0
while(i>0):
    for a in range(0,j,1):
        print(" ",end="")
    for b in range(i,0,-1):
        print("*",end="")
    for c in range(0,j+9):
        print(" ",end="")
    for a in range(0,j,1):
        print(" ",end="")
    for b in range(i,0,-1):
        print("*",end="")    
    i=i-2
    j=j+1
    print()
i=1
j=4
while(i<10):
    for a in range(j,0,-1):
        print(" ",end="")
    for b in range(0,i):
        print("*",end="")
    for c in range(j+9,0,-1):
        print(" ",end="")
    for a in range(j,0,-1):
        print(" ",end="")
    for b in range(0,i):
        print("*",end="")    
    i=i+2
    j=j-1
    print()    
    

i=9
j=0
while(i>0):
    for c in range(0,9):
        print(" ",end="")
    for a in range(0,j,1):
        print(" ",end="")
    for b in range(i,0,-1):
        print("*",end="")
    i=i-2
    j=j+1
    print()        
    
