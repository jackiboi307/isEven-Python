def isEven(num):
    return len(([""]*abs(num))[:abs(num)//2]) == len(([""]*abs(num))[abs(num)//2:])
