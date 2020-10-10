
def newPattern(n):
    for i in range(0,n+1):
        print(end=" " * n + "* " * i + "\n")
        n = n-1
        i = i + 1

newPattern(10)

