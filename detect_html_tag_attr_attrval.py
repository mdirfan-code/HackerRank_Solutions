import re
n=int(input())
s=""
for i in range(n):
    s+=input()
    
lst=list(re.findall(r'''([^\s<!-]+)<([\w]+)\s?([A-Za-z0-9='.\s/"-]+)*>''',s)) 



print()
print(lst)
print()
for t in lst:
    if("!" not in t[0]):
        print(t[1])
        if(t[2] !='' ):
            v=t[2].split()
            for i in v:
                try:
                    na,va= i.split('=')
                    print("->",na,">",va.strip("'\"/"))
                except:
                    print("->",i,"> None")