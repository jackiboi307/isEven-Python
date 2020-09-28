def isEven(num):
    x = "X" * num
    x = list(x)
    try:
        x[len(x)//2] = " "
    except:
        return True
    x = "".join(x)
    try:
        return not x.split(" ")[0] == x.split(" ")[1]
    except:
        return False
