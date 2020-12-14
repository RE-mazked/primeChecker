from math import trunc
import sys

def foundPrime(num):
    nums = [2]
    i = 3
    primaryBool = True
    while len(nums) < num:
        m = trunc(i/2)
        for x in nums:
            if m >= x:
                if (i % x) == 0:
                    primaryBool = False
                    break
            else:
                break
        if primaryBool:
            nums.append(i)
        else:
            primaryBool = True
        i += 1
    print(nums)
            
if __name__ == '__main__':
    if len(sys.argv) < 2:
        foundPrime(1000)
    else:
        if type(sys.argv[1]) == type(int):
            foundPrime(sys.argv[1])
        else:
            print("Please introduce a number")