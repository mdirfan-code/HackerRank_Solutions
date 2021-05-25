
import re
import email.utils

n=int(input())
for _ in range(n):
    name,em=tuple(email.utils.parseaddr(input()))
    if(re.match(r'[A-Za-z][a-zA-Z0-9._-]+@[A-Za-z]+\.[A-Za-z]{1,3}$',em)):
        print (email.utils.formataddr((name,em)))
        
