def minrefills(x,n,L):
    numRefills = 0
    currentRefill = 0
    while currentRefill<=n:
        lastRefill=currentRefill
        while currentRefill<=n and x[currentRefill+1]-x[lastRefill]<=L:
            currentRefill+=1
        if currentRefill == lastRefill:
            return -1
        if currentRefill<=n:
            numRefills+=1
    return numRefills
d = int(input())
L = int(input())
n = int(input())
x =[0]+ list(map(int,input().split())) + [d]
print(minrefills(x,n,L))
