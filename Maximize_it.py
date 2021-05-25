from itertools import product
k,m=map(int,input().split())
maxo=0
ls=[]
for _ in range(k):
    ls.append(list(map(int,input().split())))
co_ls=list(product(*ls))
print(co_ls)
'''for i in co_ls:
    r=0
    for j in i:
       r+=j**2
    if(maxo<r%m):
        maxo=r%m
print(maxo)'''            