def fun(s):
    try:
        frag1,frag2=s.split('@')
        frag2,frag3=frag2.split('.')
        if(len(frag3) > 3):
            return False
        for i in frag2:
            if not ((i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9')) :
                return False
        for i in frag1:
            if not ((i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9') or i=='-' or i=='_') :
                return False
        return True    
    except:
        return False            
            
        
            

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)