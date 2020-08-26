'''
The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
***Input Format:*** The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the
value and the weight of 𝑖-th item, respectively.
'''
***hello***
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
    



    

