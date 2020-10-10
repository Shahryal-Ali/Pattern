# Pattern
Created pattern using python For Loop and by creating function 

I wrote this to learn more about for loop and functions in python 


def newPattern(n):
    for i in range(0,n+1):
        print(end=" " * n + "* " * i + "\n")
        n = n-1
        i = i + 1

newPattern(10)
