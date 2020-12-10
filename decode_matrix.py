

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
c_st=""
for i in range(m):
     for j in range(n):
        c_st+=matrix[j][i]
st=""

g=2
i=0   
l=-1  
while(i < len(c_st)):
    if(not c_st[i].isalnum()):

        if(g==0):
            l=i
            g=1
        elif(g==2):
            st+=c_st[i]
        i+=1    
        continue
    if(g==1):
        st+=' '
    g=0
    st+=c_st[i]
    i+=1
if(l!=-1):    
    print(st+c_st[l:])
else:
    print(st)    