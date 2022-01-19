def main():
    lst=[]
    lst2=[]
    n=2
    while n<1000000:
        result=longestChainNumber(n)
        lst.append(result[0])
        lst2.append(result[1])
        n+=1
    great=max(lst2)
    greatest=lst2.index(great)
    print(lst[greatest])
def longestChainNumber(i):
    first=i
    n=0
    while True:
        if i==1:
            break
        if i%2==0:
            i=i/2
        else:
            i=3*i+1
        n+=1
    return [first,n]



if __name__=="__main__":main()