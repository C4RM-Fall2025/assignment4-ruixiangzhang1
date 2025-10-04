

def FizzBuzz(start, finish):
    outlist = []
    for n in range(start, finish + 1):
        s = ""
        if n % 3 == 0:
            s += "fizz"
        if n % 5 == 0:
            s += "buzz"
        if not s:
            s = str(n)
        outlist.append(s)
    return outlist
