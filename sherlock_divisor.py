for i in range(1,101):
    c=0
    n=i
    while(n%2==0):
        n//=2
        c+=1
    print(i,c,sep=" = ")