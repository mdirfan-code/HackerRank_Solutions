import re
       
n=int(input())
s=""
for i in range(n):
    s+=(input()+'\n')

s=re.sub(r'[^|&][|]{2}[\s][^&|]'," or ",s)    
s=re.sub(r'[^&|][&]{2}[\s][^&|]'," and ",s)    
print(s)