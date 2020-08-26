def max_num_prize(n):
    l = list()
    i=1
    while n>0:
        if n>=i:
            l.append(i)
            n-=i
            i+=1
            
        else:
            remove_element = i - n
            l.remove(remove_element)
            n+=remove_element
            
    return l
         
    
n = int(input())
l = max_num_prize(n)
print(len(l))
s = [str(i) for i in l]
print(" ".join(s))
