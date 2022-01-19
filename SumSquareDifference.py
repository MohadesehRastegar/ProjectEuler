#!/usr/bin/evn python3

def main():
    resultOfPower=0
    for i in range(1,101):
        resultOfPower+=power(i)
    x=0
    for i in range(1,101):
        x+=i
    square=power(x)
    total=resultOfPower-square
    print(total)

def power(i):
    result=0
    result+=i**2
    return result

if __name__=="__main__":main()