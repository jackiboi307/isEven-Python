def isEven(num):
    return len(([""]*num)[:num//2]) == len(([""]*num)[num//2:])
    
# doesn't work for any negative
