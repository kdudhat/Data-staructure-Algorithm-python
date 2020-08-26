def adsrevenue(n,a,b):
    a.sort()
    b.sort()
    c = [i*j for i,j in zip(a,b)]
    return sum(c)
    


n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

print(adsrevenue(n,a,b))
