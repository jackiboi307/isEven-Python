def isEven(num):
    s = ([" "] * num)[:]
    s[num//2] = "X"
    return not len(("".join(s).split("X"))[0]) == len(("".join(s).split("X"))[1])
    
# doesn't work for the number 0 or any negative
