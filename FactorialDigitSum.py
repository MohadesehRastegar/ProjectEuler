#!/usr/bin/env python3

def main():
    result=str(factorial(100))
    sum=0
    for i in result:
        sum+=int(i)
    return sum ,"\U0001F60D"
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return  n*factorial(n-1)

if __name__=="__main__":print(main())