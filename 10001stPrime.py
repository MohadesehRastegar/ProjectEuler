#!/usr/bin/evn python 3
def main():
    lst=[2]
    i=2
    while True:
        result=aval(i)
        if result==True:
            lst.append(i)
        try:
            print(lst[10000])
            break
        except IndexError:        
            i+=1

def aval(i):
    for j in range(2,i):
        if i%j==0:
            return False
    return True
if __name__=="__main__":main()