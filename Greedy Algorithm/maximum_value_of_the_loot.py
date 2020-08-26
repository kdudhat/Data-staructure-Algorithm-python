n,total_weight = map(int, input().split())
total_value = 0
l = list()
for i in range(n):
    value,weight = map(int,input().split())
    l.append([value,weight,value/weight])

def Sort(sub_li):
    return(sorted(sub_li, key = lambda x: x[2], reverse=True))	 
l = Sort(l)

for i in l:
    if total_weight == 0:
         break
    if total_weight<i[1]:
        x = i[1]/total_weight
        total_value+=i[0]/x
        total_weight=0
    else:
        total_value+=i[0]
        total_weight-=i[1]
        
print(total_value)
    



    

