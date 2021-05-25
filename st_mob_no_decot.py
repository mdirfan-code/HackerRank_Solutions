def wrapper(f):
    def fun(l):
        ls=[]
        for i in l:
            if(len(i) == 10):
                ls.append("+91 "+i[:5]+" "+i[5:])
            else:
                if(i[0]=="0"):
                    ls.append("+91 "+i[1:6]+" "+i[6:])
                elif(i[0]=="+"):
                    ls.append(i[:3]+" "+i[3:8]+" "+i[8:])
                elif(i[0]=="9"):
                    ls.append("+"+i[:2]+" "+i[2:7]+" "+i[7:])    
        r = f(ls)
        print(ls)
        return r                                   
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


