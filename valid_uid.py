import re
n=int(input())
lst=[]
for i in range(n):
    s=input()
    lst.append(re.findall(r'.*(.).*\1.*',s))

    ''' if  re.search(r'^[a-zA-Z0-9]{10}$',s) and len((re.findall(r'[A-Z]',s))) >= 2 and len((re.findall(r'[0-9]',s))) >= 3  and not len(re.findall(r'([\w])\1\w*\1',s)):
        print("Valid")
    else:
        print("Invalid")'''
print(lst)