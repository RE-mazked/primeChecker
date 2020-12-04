import sys

def checkPrimary(num):
    res = 0
    divBy = 0
    primaryBool = False
    primaryBooltemp = False
    for i in range(0, num):
        i += 1  
        res_han = num/i
        if int(res_han) == res_han and res_han != 1:
            if primaryBooltemp:
                primaryBool = True
                divBy = i
                break
            primaryBooltemp = True
        else:
            res += res_han
    return primaryBool, divBy, res


if __name__ == '__main__':
    if len(sys.argv) == 1:
        num = int(input("Write a number:"))
    else:
        num = int(sys.argv[1])

    primaryBool, divBy, res = checkPrimary(num)
    if primaryBool:
        print(f'Not prime primary, divisible by {divBy}')
    else:
        print('Prime')