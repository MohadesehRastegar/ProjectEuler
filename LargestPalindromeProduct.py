#!/usr/bin/env python3
#This file is written by Mohadeseh
def main():
    #What are palindromic numbers?
    #Numbers that could be read the same from both sides, like 101 or 9009
    lst = list()
    for i in range(100,1000):
        for j in range(100, 1000):
            reversedOne = palindrome(i * j) #This is the reverse result of the product
            if i * j == reversedOne: #Here we check if reversed result is the same as the product it self
                lst.append(i * j) #Adding every number which are palindromic

    print("The answer is", max(lst))

#Returns a reversed number of the number
def palindrome(number):
    result = 0
    while number >= 1:
        result = (result * 10) + (number % 10)
        number = number // 10
    else:
        return result

if __name__ == "__main__": main()