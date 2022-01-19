#!/usr/bin/env python3

def main():
    number=Power()
    number=set(number)
    number=list(number)
    print(len(number))
    
def Power():
    lst=[]
    for i in range(2,101):
        for j in range(2,101):
            lst.append(i**j)
    return lst

if __name__=="__main__":main()