import re
n=int(input())
s=""
for i in range(n):
    s+=input()
    
lst=list(re.findall(r'''<(\w+)\s?([A-Za-z0-9='.\s/"-]+)*>''',s)) 
    
for t in lst:
    if t[2] == '/':
        print("Empty :",t[1])
        continue
    elif t[0] == '/':
        print("End   :",t[1])
        continue
    elif t[0] == '':
        print("Start :",t[1])
    if(t[2] !=''):
        v=list(map(tuple,*t[2].split()))
        """for i in v:
            try:
                na,va= i.split('=')
                print("->",na,">",va.strip("'\""))
            except:
                print("->",i,"> None")"""
        print(v)
