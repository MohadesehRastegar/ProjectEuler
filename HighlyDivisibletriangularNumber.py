#!/usr/bin/env python3

import math
def main():
    print(triangel())


def triangel():
    n = 1
    while True:
        lst = []
        result = (n * (n + 1)) / 2
        sqrt=math.sqrt(result)
        lst.append(result)
        for i in range(1, int(sqrt+1)):
            if result % i == 0:
                lst.append(result//i)
                lst.append(i)
        if len(lst) > 500:
            return result

        else:
            n += 1


if __name__ == "__main__": main()