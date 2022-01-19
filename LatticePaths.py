
memo1={}
memo={}
def main(x,y):
    if x==0  or y==0:
        return 1
    if x in memo1:
        result1=int(memo1[x])
        result2=int(memo[y])
        if result1==result2:
      
            return memo1[x]
    else:
        answer= main(x,y-1)+main(x-1,y)
        memo1[x]=answer
        memo[y]=answer
        return answer

print(main(2,2))